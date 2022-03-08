# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['wacky', 'wacky.basic_types', 'wacky.enums', 'wacky.hashing', 'wacky.structs']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.4,<9.0.0',
 'construct-typing>=0.5.2,<0.6.0',
 'ruamel.yaml>=0.17.21,<0.18.0']

entry_points = \
{'console_scripts': ['wacky = wacky.cli:main']}

setup_kwargs = {
    'name': 'wacky',
    'version': '1.0.1',
    'description': 'Wacca DataTable files loading + dumping',
    'long_description': '# Wacky\n\nWacca DataTable files loading + dumping lib\n\nSpecifically geared towards files :\n\n- created by / for UE 4.19\n- split in `.uasset` + `.uexp` pairs\n- only containing DataTable exports\n\n## Installing\n\n```shell-session\npip install wacky\n```\n\n## Command Line Usage\n\n### Unpacking\n\n```shell-session\n$ wacky unpack [OPTIONS] UASSET UEXP\n```\n\nThis converts the useful data inside `UASSET` and `UEXP` to a yaml (or json) file you can edit and then use to repack\n\nOptions:\n  - `--json` : Output json instead of yaml\n  - `-o FILENAME`, `--output FILENAME` : Output to a specific file (instead of to stdout)\n  - `--help`: Show a help message and exit.\n\n### Modifying\n\nJust use a text editor to change the file you\'ve created with the previous command\n\n### Repacking\n\n```shell-session\n$ wacky repack [OPTIONS] SRC_UASSET SRC_UEXP NEW_DATA DST_UASSET DST_UEXP\n```\n\nThis creates new modified `.uasset` and `.uexp` files by using `SRC_UASSET` and `SRC_UEXP` as templates and applying the changes specified by `NEW_DATA`\n\nOptions:\n  - `--help`: Show a help message and exit.\n\n## Python API\n\n```python\n>>> from wacky import load, dump\n>>> package = load(uasset=open(..., "rb"), uexp=open(..., "rb"))\n>>> ... # Do stuff with `package`\n>>> dump(package, uasset=open(..., "wb"), uexp=open(..., "wb"))\n```\n\n\n## Folder Contents\n\n| File / Folder | Description |\n|---------------|-------------|\n| src/ | Sources |\n| tests/ | unit tests, with example `.uasset` and `.uexp` files |\n| utils/ | Things worth keeping around |\n| .flake8 | [Flake8](https://flake8.pycqa.org/en/latest/) config |\n| .gitignore | list of file patterns git ignores |\n| CHANGELOG.md | Changelog |\n| poetry.lock | Precise info about every dependency or sub-dependency, generated by [poetry](https://python-poetry.org/), don\'t modify yourself |\n| pyproject.toml | Projet description file, mostly managed by [poetry](https://python-poetry.org/) |\n| README.md | The file you are reading right now |\n| UE4.ksy |\xa0Definition of the .uasset + .uexp file structure using [Kaitai Struct](https://kaitai.io/), for documentation and preservation purposes |',
    'author': 'Stepland',
    'author_email': '10530295-Buggyroom@users.noreply.gitlab.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/Buggyroom/wacky',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
