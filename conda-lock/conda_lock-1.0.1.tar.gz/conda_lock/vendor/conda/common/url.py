# -*- coding: utf-8 -*-
# Copyright (C) 2012 Anaconda, Inc
# SPDX-License-Identifier: BSD-3-Clause
from __future__ import absolute_import, division, print_function, unicode_literals

import codecs
from getpass import getpass
from os.path import abspath, expanduser
import re
import socket

from .compat import input, on_win
from .path import split_filename, strip_pkg_extension
from ..auxlib.decorators import memoize
from .._vendor.urllib3.exceptions import LocationParseError
from .._vendor.urllib3.util.url import Url, parse_url

try:  # pragma: py2 no cover
    # Python 3
    from urllib.parse import (quote, quote_plus, unquote, unquote_plus)
except ImportError:  # pragma: py3 no cover
    # Python 2
    from urllib import (quote, quote_plus, unquote, unquote_plus)  # NOQA


def hex_octal_to_int(ho):
    ho = ord(ho)
    o0 = ord('0')
    o9 = ord('9')
    oA = ord('A')
    oF = ord('F')
    res = ho - o0 if ho >= o0 and ho <= o9 else (ho - oA + 10) if ho >= oA and ho <= oF else None
    return res


@memoize
def percent_decode(path):

    # This is not fast so avoid when we can.
    if '%' not in path:
        return path
    ranges = []
    for m in re.finditer(r'(%[0-9A-F]{2})', path):
        ranges.append((m.start(), m.end()))
    if not len(ranges):
        return path

    # Sorry! Correctness is more important than speed at the moment.
    # Should use a map + lambda eventually.
    result = b''
    skips = 0
    for i, c in enumerate(path):
        if skips > 0:
            skips -= 1
            continue
        c = c.encode('ascii')
        emit = c
        if c == b'%':
            for r in ranges:
                if i == r[0]:
                    import struct
                    emit = struct.pack(
                        "B", hex_octal_to_int(path[i+1])*16 + hex_octal_to_int(path[i+2]))
                    skips = 2
                    break
        if emit:
            result += emit
    return codecs.utf_8_decode(result)[0]


file_scheme = 'file://'

# Keeping this around for now, need to combine with the same function in conda/common/path.py
"""
def url_to_path(url):
    assert url.startswith(file_scheme), "{} is not a file-scheme URL".format(url)
    decoded = percent_decode(url[len(file_scheme):])
    if decoded.startswith('/') and decoded[2] == ':':
        # A Windows path.
        decoded.replace('/', '\\')
    return decoded
"""


@memoize
def path_to_url(path):
    if not path:
        raise ValueError('Not allowed: %r' % path)
    if path.startswith(file_scheme):
        try:
            path.decode('ascii')
        except UnicodeDecodeError:
            raise ValueError('Non-ascii not allowed for things claiming to be URLs: %r' % path)
        return path
    path = abspath(expanduser(path)).replace('\\', '/')
    # We do not use urljoin here because we want to take our own
    # *very* explicit control of how paths get encoded into URLs.
    #   We should not follow any RFCs on how to encode and decode
    # them, we just need to make sure we can represent them in a
    # way that will not cause problems for whatever amount of
    # urllib processing we *do* need to do on them (which should
    # be none anyway, but I doubt that is the case). I have gone
    # for ASCII and % encoding of everything not alphanumeric or
    # not in `!'()*-._/:`. This should be pretty save.
    #
    # To avoid risking breaking the internet, this code only runs
    # for `file://` URLs.
    #
    percent_encode_chars = "!'()*-._/\\:"
    percent_encode = lambda s: "".join(["%%%02X" % ord(c), c]
                                       [c < "{" and c.isalnum() or c in percent_encode_chars]
                                       for c in s)
    if any(ord(char) >= 128 for char in path):
        path = percent_encode(path.decode('unicode-escape')
                              if hasattr(path, 'decode')
                              else bytes(path, "utf-8").decode('unicode-escape'))

    # https://blogs.msdn.microsoft.com/ie/2006/12/06/file-uris-in-windows/
    if len(path) > 1 and path[1] == ':':
        path = file_scheme + '/' + path
    else:
        path = file_scheme + path
    return path


@memoize
def urlparse(url):
    if on_win and url.startswith('file:'):
        url.replace('\\', '/')
    return parse_url(url)


def url_to_s3_info(url):
    """Convert an s3 url to a tuple of bucket and key.

    Examples:
        >>> url_to_s3_info("s3://bucket-name.bucket/here/is/the/key")
        ('bucket-name.bucket', '/here/is/the/key')
    """
    parsed_url = parse_url(url)
    assert parsed_url.scheme == 's3', "You can only use s3: urls (not %r)" % url
    bucket, key = parsed_url.host, parsed_url.path
    return bucket, key


def is_url(url):
    """
    Examples:
        >>> is_url(None)
        False
        >>> is_url("s3://some/bucket")
        True
    """
    if not url:
        return False
    try:
        return urlparse(url).scheme is not None
    except LocationParseError:
        return False


def is_ipv4_address(string_ip):
    """
    Examples:
        >>> [is_ipv4_address(ip) for ip in ('8.8.8.8', '192.168.10.10', '255.255.255.255')]
        [True, True, True]
        >>> [is_ipv4_address(ip) for ip in ('8.8.8', '192.168.10.10.20', '256.255.255.255', '::1')]
        [False, False, False, False]
    """
    try:
        socket.inet_aton(string_ip)
    except socket.error:
        return False
    return string_ip.count('.') == 3


def is_ipv6_address(string_ip):
    """
    Examples:
        >> [is_ipv6_address(ip) for ip in ('::1', '2001:db8:85a3::370:7334', '1234:'*7+'1234')]
        [True, True, True]
        >> [is_ipv6_address(ip) for ip in ('192.168.10.10', '1234:'*8+'1234')]
        [False, False]
    """
    try:
        inet_pton = socket.inet_pton
    except AttributeError:
        return is_ipv6_address_win_py27(string_ip)
    try:
        inet_pton(socket.AF_INET6, string_ip)
    except socket.error:
        return False
    return True


def is_ipv6_address_win_py27(string_ip):
    """
    Examples:
        >>> [is_ipv6_address_win_py27(ip) for ip in ('::1', '1234:'*7+'1234')]
        [True, True]
        >>> [is_ipv6_address_win_py27(ip) for ip in ('192.168.10.10', '1234:'*8+'1234')]
        [False, False]
    """
    # python 2.7 on windows does not have socket.inet_pton
    return bool(re.match(r""  # lgtm [py/regex/unmatchable-dollar]
                         r"^(((?=.*(::))(?!.*\3.+\3))\3?|[\dA-F]{1,4}:)"
                         r"([\dA-F]{1,4}(\3|:\b)|\2){5}"
                         r"(([\dA-F]{1,4}(\3|:\b|$)|\2){2}|"
                         r"(((2[0-4]|1\d|[1-9])?\d|25[0-5])\.?\b){4})\Z",
                         string_ip,
                         flags=re.DOTALL | re.IGNORECASE))


def is_ip_address(string_ip):
    """
    Examples:
        >> is_ip_address('192.168.10.10')
        True
        >> is_ip_address('::1')
        True
        >> is_ip_address('www.google.com')
        False
    """
    return is_ipv4_address(string_ip) or is_ipv6_address(string_ip)


def join(*args):
    start = '/' if not args[0] or args[0].startswith('/') else ''
    return start + '/'.join(y for y in (x.strip('/') for x in args if x) if y)


join_url = join


def has_scheme(value):
    return re.match(r'[a-z][a-z0-9]{0,11}://', value)


def strip_scheme(url):
    """
    Examples:
        >>> strip_scheme("https://www.conda.io")
        'www.conda.io'
        >>> strip_scheme("s3://some.bucket/plus/a/path.ext")
        'some.bucket/plus/a/path.ext'
    """
    return url.split('://', 1)[-1]


def mask_anaconda_token(url):
    _, token = split_anaconda_token(url)
    return url.replace(token, "<TOKEN>", 1) if token else url


def split_anaconda_token(url):
    """
    Examples:
        >>> split_anaconda_token("https://1.2.3.4/t/tk-123-456/path")
        (u'https://1.2.3.4/path', u'tk-123-456')
        >>> split_anaconda_token("https://1.2.3.4/t//path")
        (u'https://1.2.3.4/path', u'')
        >>> split_anaconda_token("https://some.domain/api/t/tk-123-456/path")
        (u'https://some.domain/api/path', u'tk-123-456')
        >>> split_anaconda_token("https://1.2.3.4/conda/t/tk-123-456/path")
        (u'https://1.2.3.4/conda/path', u'tk-123-456')
        >>> split_anaconda_token("https://1.2.3.4/path")
        (u'https://1.2.3.4/path', None)
        >>> split_anaconda_token("https://10.2.3.4:8080/conda/t/tk-123-45")
        (u'https://10.2.3.4:8080/conda', u'tk-123-45')
    """
    _token_match = re.search(r'/t/([a-zA-Z0-9-]*)', url)
    token = _token_match.groups()[0] if _token_match else None
    cleaned_url = url.replace('/t/' + token, '', 1) if token is not None else url
    return cleaned_url.rstrip('/'), token


def split_platform(known_subdirs, url):
    """

    Examples:
        >>> from conda.base.constants import KNOWN_SUBDIRS
        >>> split_platform(KNOWN_SUBDIRS, "https://1.2.3.4/t/tk-123/linux-ppc64le/path")
        (u'https://1.2.3.4/t/tk-123/path', u'linux-ppc64le')

    """
    _platform_match = _split_platform_re(known_subdirs).search(url)
    platform = _platform_match.groups()[0] if _platform_match else None
    cleaned_url = url.replace('/' + platform, '', 1) if platform is not None else url
    return cleaned_url.rstrip('/'), platform


@memoize
def _split_platform_re(known_subdirs):
    _platform_match_regex = r'/(%s)(?:/|$)' % r'|'.join(r'%s' % d for d in known_subdirs)
    return re.compile(_platform_match_regex, re.IGNORECASE)


def has_platform(url, known_subdirs):
    url_no_package_name, _ = split_filename(url)
    if not url_no_package_name:
        return None
    maybe_a_platform = url_no_package_name.rsplit('/', 1)[-1]
    return maybe_a_platform in known_subdirs and maybe_a_platform or None


def split_scheme_auth_token(url):
    """
    Examples:
        >>> split_scheme_auth_token("https://u:p@conda.io/t/x1029384756/more/path")
        ('conda.io/more/path', 'https', 'u:p', 'x1029384756')
        >>> split_scheme_auth_token(None)
        (None, None, None, None)
    """
    if not url:
        return None, None, None, None
    cleaned_url, token = split_anaconda_token(url)
    url_parts = urlparse(cleaned_url)
    remainder_url = Url(host=url_parts.host, port=url_parts.port, path=url_parts.path,
                        query=url_parts.query).url
    return remainder_url, url_parts.scheme, url_parts.auth, token


def split_conda_url_easy_parts(known_subdirs, url):
    # scheme, auth, token, platform, package_filename, host, port, path, query
    cleaned_url, token = split_anaconda_token(url)
    cleaned_url, platform = split_platform(known_subdirs, cleaned_url)
    _, ext = strip_pkg_extension(cleaned_url)
    cleaned_url, package_filename = cleaned_url.rsplit('/', 1) if ext else (cleaned_url, None)

    # TODO: split out namespace using regex

    url_parts = urlparse(cleaned_url)

    return (url_parts.scheme, url_parts.auth, token, platform, package_filename, url_parts.host,
            url_parts.port, url_parts.path, url_parts.query)


@memoize
def get_proxy_username_and_pass(scheme):
    username = input("\n%s proxy username: " % scheme)
    passwd = getpass("Password: ")
    return username, passwd


def add_username_and_password(url, username, password):
    url_parts = parse_url(url)._asdict()
    url_parts['auth'] = username + ':' + quote(password, '')
    return Url(**url_parts).url


def maybe_add_auth(url, auth, force=False):
    """Add auth if the url doesn't currently have it.

    By default, does not replace auth if it already exists.  Setting ``force`` to ``True``
    overrides this behavior.

    Examples:
        >>> maybe_add_auth("https://www.conda.io", "user:passwd")
        'https://user:passwd@www.conda.io'
        >>> maybe_add_auth("https://www.conda.io", "")
        'https://www.conda.io'
    """
    if not auth:
        return url
    url_parts = urlparse(url)._asdict()
    if url_parts['auth'] and not force:
        return url
    url_parts['auth'] = auth
    return Url(**url_parts).url


def maybe_unquote(url):
    return unquote_plus(remove_auth(url)) if url else url


def remove_auth(url):
    url_parts = parse_url(url)._asdict()
    if url_parts['auth']:
        del url_parts['auth']
    return Url(**url_parts).url


if __name__ == "__main__":
    import doctest
    doctest.testmod()
