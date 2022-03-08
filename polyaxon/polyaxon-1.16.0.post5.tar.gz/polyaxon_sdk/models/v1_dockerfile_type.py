#!/usr/bin/python
#
# Copyright 2018-2021 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Polyaxon SDKs and REST API specification.

    Polyaxon SDKs and REST API specification.  # noqa: E501

    The version of the OpenAPI document: 1.16.0
    Contact: contact@polyaxon.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from polyaxon_sdk.configuration import Configuration


class V1DockerfileType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'image': 'str',
        'env': 'dict(str, str)',
        'path': 'list[str]',
        'copy': 'list[object]',
        'post_run_copy': 'list[object]',
        'run': 'list[str]',
        'lang_env': 'str',
        'uid': 'int',
        'gid': 'int',
        'username': 'int',
        'filename': 'str',
        'workdir': 'str',
        'workdir_path': 'str',
        'shell': 'str'
    }

    attribute_map = {
        'image': 'image',
        'env': 'env',
        'path': 'path',
        'copy': 'copy',
        'post_run_copy': 'post_run_copy',
        'run': 'run',
        'lang_env': 'langEnv',
        'uid': 'uid',
        'gid': 'gid',
        'username': 'username',
        'filename': 'filename',
        'workdir': 'workdir',
        'workdir_path': 'workdirPath',
        'shell': 'shell'
    }

    def __init__(self, image=None, env=None, path=None, copy=None, post_run_copy=None, run=None, lang_env=None, uid=None, gid=None, username=None, filename=None, workdir=None, workdir_path=None, shell=None, local_vars_configuration=None):  # noqa: E501
        """V1DockerfileType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._image = None
        self._env = None
        self._path = None
        self._copy = None
        self._post_run_copy = None
        self._run = None
        self._lang_env = None
        self._uid = None
        self._gid = None
        self._username = None
        self._filename = None
        self._workdir = None
        self._workdir_path = None
        self._shell = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if env is not None:
            self.env = env
        if path is not None:
            self.path = path
        if copy is not None:
            self.copy = copy
        if post_run_copy is not None:
            self.post_run_copy = post_run_copy
        if run is not None:
            self.run = run
        if lang_env is not None:
            self.lang_env = lang_env
        if uid is not None:
            self.uid = uid
        if gid is not None:
            self.gid = gid
        if username is not None:
            self.username = username
        if filename is not None:
            self.filename = filename
        if workdir is not None:
            self.workdir = workdir
        if workdir_path is not None:
            self.workdir_path = workdir_path
        if shell is not None:
            self.shell = shell

    @property
    def image(self):
        """Gets the image of this V1DockerfileType.  # noqa: E501


        :return: The image of this V1DockerfileType.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this V1DockerfileType.


        :param image: The image of this V1DockerfileType.  # noqa: E501
        :type image: str
        """

        self._image = image

    @property
    def env(self):
        """Gets the env of this V1DockerfileType.  # noqa: E501


        :return: The env of this V1DockerfileType.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this V1DockerfileType.


        :param env: The env of this V1DockerfileType.  # noqa: E501
        :type env: dict(str, str)
        """

        self._env = env

    @property
    def path(self):
        """Gets the path of this V1DockerfileType.  # noqa: E501


        :return: The path of this V1DockerfileType.  # noqa: E501
        :rtype: list[str]
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1DockerfileType.


        :param path: The path of this V1DockerfileType.  # noqa: E501
        :type path: list[str]
        """

        self._path = path

    @property
    def copy(self):
        """Gets the copy of this V1DockerfileType.  # noqa: E501


        :return: The copy of this V1DockerfileType.  # noqa: E501
        :rtype: list[object]
        """
        return self._copy

    @copy.setter
    def copy(self, copy):
        """Sets the copy of this V1DockerfileType.


        :param copy: The copy of this V1DockerfileType.  # noqa: E501
        :type copy: list[object]
        """

        self._copy = copy

    @property
    def post_run_copy(self):
        """Gets the post_run_copy of this V1DockerfileType.  # noqa: E501


        :return: The post_run_copy of this V1DockerfileType.  # noqa: E501
        :rtype: list[object]
        """
        return self._post_run_copy

    @post_run_copy.setter
    def post_run_copy(self, post_run_copy):
        """Sets the post_run_copy of this V1DockerfileType.


        :param post_run_copy: The post_run_copy of this V1DockerfileType.  # noqa: E501
        :type post_run_copy: list[object]
        """

        self._post_run_copy = post_run_copy

    @property
    def run(self):
        """Gets the run of this V1DockerfileType.  # noqa: E501


        :return: The run of this V1DockerfileType.  # noqa: E501
        :rtype: list[str]
        """
        return self._run

    @run.setter
    def run(self, run):
        """Sets the run of this V1DockerfileType.


        :param run: The run of this V1DockerfileType.  # noqa: E501
        :type run: list[str]
        """

        self._run = run

    @property
    def lang_env(self):
        """Gets the lang_env of this V1DockerfileType.  # noqa: E501


        :return: The lang_env of this V1DockerfileType.  # noqa: E501
        :rtype: str
        """
        return self._lang_env

    @lang_env.setter
    def lang_env(self, lang_env):
        """Sets the lang_env of this V1DockerfileType.


        :param lang_env: The lang_env of this V1DockerfileType.  # noqa: E501
        :type lang_env: str
        """

        self._lang_env = lang_env

    @property
    def uid(self):
        """Gets the uid of this V1DockerfileType.  # noqa: E501


        :return: The uid of this V1DockerfileType.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this V1DockerfileType.


        :param uid: The uid of this V1DockerfileType.  # noqa: E501
        :type uid: int
        """

        self._uid = uid

    @property
    def gid(self):
        """Gets the gid of this V1DockerfileType.  # noqa: E501


        :return: The gid of this V1DockerfileType.  # noqa: E501
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this V1DockerfileType.


        :param gid: The gid of this V1DockerfileType.  # noqa: E501
        :type gid: int
        """

        self._gid = gid

    @property
    def username(self):
        """Gets the username of this V1DockerfileType.  # noqa: E501


        :return: The username of this V1DockerfileType.  # noqa: E501
        :rtype: int
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this V1DockerfileType.


        :param username: The username of this V1DockerfileType.  # noqa: E501
        :type username: int
        """

        self._username = username

    @property
    def filename(self):
        """Gets the filename of this V1DockerfileType.  # noqa: E501


        :return: The filename of this V1DockerfileType.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this V1DockerfileType.


        :param filename: The filename of this V1DockerfileType.  # noqa: E501
        :type filename: str
        """

        self._filename = filename

    @property
    def workdir(self):
        """Gets the workdir of this V1DockerfileType.  # noqa: E501


        :return: The workdir of this V1DockerfileType.  # noqa: E501
        :rtype: str
        """
        return self._workdir

    @workdir.setter
    def workdir(self, workdir):
        """Sets the workdir of this V1DockerfileType.


        :param workdir: The workdir of this V1DockerfileType.  # noqa: E501
        :type workdir: str
        """

        self._workdir = workdir

    @property
    def workdir_path(self):
        """Gets the workdir_path of this V1DockerfileType.  # noqa: E501


        :return: The workdir_path of this V1DockerfileType.  # noqa: E501
        :rtype: str
        """
        return self._workdir_path

    @workdir_path.setter
    def workdir_path(self, workdir_path):
        """Sets the workdir_path of this V1DockerfileType.


        :param workdir_path: The workdir_path of this V1DockerfileType.  # noqa: E501
        :type workdir_path: str
        """

        self._workdir_path = workdir_path

    @property
    def shell(self):
        """Gets the shell of this V1DockerfileType.  # noqa: E501


        :return: The shell of this V1DockerfileType.  # noqa: E501
        :rtype: str
        """
        return self._shell

    @shell.setter
    def shell(self, shell):
        """Sets the shell of this V1DockerfileType.


        :param shell: The shell of this V1DockerfileType.  # noqa: E501
        :type shell: str
        """

        self._shell = shell

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1DockerfileType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1DockerfileType):
            return True

        return self.to_dict() != other.to_dict()
