import setuptools
from pathlib import Path

setuptools.setup(
    name="osepdf",
    version=1.0,
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["tests", "data"])
)
