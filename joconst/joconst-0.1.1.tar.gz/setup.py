# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['joconst']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'joconst',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'FangyangJz',
    'author_email': 'fangyang.jing@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
