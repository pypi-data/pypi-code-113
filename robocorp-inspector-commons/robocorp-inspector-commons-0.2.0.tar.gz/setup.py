# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['inspector_commons', 'inspector_commons.api', 'inspector_commons.bridge']

package_data = \
{'': ['*'], 'inspector_commons': ['static/resources/*']}

install_requires = \
['requests>=2.25.1,<3.0.0',
 'rpaframework-core>=6.3.2,<7.0.0',
 'typing-extensions>=3.10.0,<4.0.0']

setup_kwargs = {
    'name': 'robocorp-inspector-commons',
    'version': '0.2.0',
    'description': 'Robocorp Inspector Commons',
    'long_description': '# Robocorp Inspector Commons\n\nRobocorp Inspector Commons is the commons package for Robocorp Inspector.\n\n## Development\n\nThe project uses `invoke` for overall project management, `poetry` for\npython dependencies and environments, and `npm` for Javascript dependencies\nand building.\n\nBoth `invoke` and `poetry` should be installed via pip: `pip install poetry invoke`\n\n- To see all possible tasks: `invoke --list`\n\nAll source code is hosted on [GitHub](https://github.com/robocorp/inspector-commons/).\n\n## Usage\n\nRobocorp Inspector Commons is distributed as a Python package with all browser overlay\ncomponents compiled and included statically.\n\n---\n\n<p align="center">\n  <img height="100" src="https://cdn.robocorp.com/brand/Logo/Dark%20logo%20transparent%20with%20buffer%20space/Dark%20logo%20transparent%20with%20buffer%20space.svg">\n</p>\n',
    'author': 'Robocorp',
    'author_email': 'dev@robocorp.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/robocorp/inspector',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
