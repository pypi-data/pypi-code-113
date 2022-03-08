# -*- coding: utf-8 -*-
# Copyright (C) 2012 Anaconda, Inc
# SPDX-License-Identifier: BSD-3-Clause
from __future__ import absolute_import, division, print_function, unicode_literals

from logging import getLogger
from threading import local

from . import (AuthBase, BaseAdapter, HTTPAdapter, Session, _basic_auth_str,
               extract_cookies_to_jar, get_auth_from_url, get_netrc_auth, Retry)
from .adapters.ftp import FTPAdapter
from .adapters.localfs import LocalFSAdapter
from .adapters.s3 import S3Adapter
from ..anaconda_client import read_binstar_tokens
from ...auxlib.ish import dals
from ...base.constants import CONDA_HOMEPAGE_URL
from ...base.context import context
from ...common.compat import iteritems, with_metaclass
from ...common.url import (add_username_and_password, get_proxy_username_and_pass,
                           split_anaconda_token, urlparse)
from ...exceptions import ProxyError

log = getLogger(__name__)
RETRIES = 3


CONDA_SESSION_SCHEMES = frozenset((
    "http",
    "https",
    "ftp",
    "s3",
    "file",
))

class EnforceUnusedAdapter(BaseAdapter):

    def send(self, request, *args, **kwargs):
        message = dals("""
        EnforceUnusedAdapter called with url %s
        This command is using a remote connection in offline mode.
        """ % request.url)
        raise RuntimeError(message)

    def close(self):
        raise NotImplementedError()


class CondaSessionType(type):
    """
    Takes advice from https://github.com/requests/requests/issues/1871#issuecomment-33327847
    and creates one Session instance per thread.
    """

    def __new__(mcs, name, bases, dct):
        dct['_thread_local'] = local()
        return super(CondaSessionType, mcs).__new__(mcs, name, bases, dct)

    def __call__(cls):
        try:
            return cls._thread_local.session
        except AttributeError:
            session = cls._thread_local.session = super(CondaSessionType, cls).__call__()
            return session


@with_metaclass(CondaSessionType)
class CondaSession(Session):

    def __init__(self):
        super(CondaSession, self).__init__()

        self.auth = CondaHttpAuth()  # TODO: should this just be for certain protocol adapters?

        self.proxies.update(context.proxy_servers)

        if context.offline:
            unused_adapter = EnforceUnusedAdapter()
            self.mount("http://", unused_adapter)
            self.mount("https://", unused_adapter)
            self.mount("ftp://", unused_adapter)
            self.mount("s3://", unused_adapter)

        else:
            # Configure retries
            retry = Retry(total=context.remote_max_retries,
                          backoff_factor=context.remote_backoff_factor,
                          status_forcelist=[413, 429, 500, 503],
                          raise_on_status=False)
            http_adapter = HTTPAdapter(max_retries=retry)
            self.mount("http://", http_adapter)
            self.mount("https://", http_adapter)
            self.mount("ftp://", FTPAdapter())
            self.mount("s3://", S3Adapter())

        self.mount("file://", LocalFSAdapter())

        self.headers['User-Agent'] = context.user_agent

        self.verify = context.ssl_verify

        if context.client_ssl_cert_key:
            self.cert = (context.client_ssl_cert, context.client_ssl_cert_key)
        elif context.client_ssl_cert:
            self.cert = context.client_ssl_cert


class CondaHttpAuth(AuthBase):
    # TODO: make this class thread-safe by adding some of the requests.auth.HTTPDigestAuth() code

    def __call__(self, request):
        request.url = CondaHttpAuth.add_binstar_token(request.url)
        self._apply_basic_auth(request)
        request.register_hook('response', self.handle_407)
        return request

    @staticmethod
    def _apply_basic_auth(request):
        # this logic duplicated from Session.prepare_request and PreparedRequest.prepare_auth
        url_auth = get_auth_from_url(request.url)
        auth = url_auth if any(url_auth) else None

        if auth is None:
            # look for auth information in a .netrc file
            auth = get_netrc_auth(request.url)

        if isinstance(auth, tuple) and len(auth) == 2:
            request.headers['Authorization'] = _basic_auth_str(*auth)

        return request

    @staticmethod
    def add_binstar_token(url):
        clean_url, token = split_anaconda_token(url)
        if not token and context.add_anaconda_token:
            for binstar_url, token in iteritems(read_binstar_tokens()):
                if clean_url.startswith(binstar_url):
                    log.debug("Adding anaconda token for url <%s>", clean_url)
                    from ...models.channel import Channel
                    channel = Channel(clean_url)
                    channel.token = token
                    return channel.url(with_credentials=True)
        return url

    @staticmethod
    def handle_407(response, **kwargs):  # pragma: no cover
        """
        Prompts the user for the proxy username and password and modifies the
        proxy in the session object to include it.

        This method is modeled after
          * requests.auth.HTTPDigestAuth.handle_401()
          * requests.auth.HTTPProxyAuth
          * the previous conda.fetch.handle_proxy_407()

        It both adds 'username:password' to the proxy URL, as well as adding a
        'Proxy-Authorization' header.  If any of this is incorrect, please file an issue.

        """
        # kwargs = {'verify': True, 'cert': None, 'proxies': OrderedDict(), 'stream': False,
        #           'timeout': (3.05, 60)}

        if response.status_code != 407:
            return response

        # Consume content and release the original connection
        # to allow our new request to reuse the same one.
        response.content
        response.close()

        proxies = kwargs.pop('proxies')

        proxy_scheme = urlparse(response.url).scheme
        if proxy_scheme not in proxies:
            raise ProxyError(dals("""
            Could not find a proxy for %r. See
            %s/docs/html#configure-conda-for-use-behind-a-proxy-server
            for more information on how to configure proxies.
            """ % (proxy_scheme, CONDA_HOMEPAGE_URL)))

        # fix-up proxy_url with username & password
        proxy_url = proxies[proxy_scheme]
        username, password = get_proxy_username_and_pass(proxy_scheme)
        proxy_url = add_username_and_password(proxy_url, username, password)
        proxy_authorization_header = _basic_auth_str(username, password)
        proxies[proxy_scheme] = proxy_url
        kwargs['proxies'] = proxies

        prep = response.request.copy()
        extract_cookies_to_jar(prep._cookies, response.request, response.raw)
        prep.prepare_cookies(prep._cookies)
        prep.headers['Proxy-Authorization'] = proxy_authorization_header

        _response = response.connection.send(prep, **kwargs)
        _response.history.append(response)
        _response.request = prep

        return _response
