import os

import setuptools

base_dir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(base_dir, "README.md"), 'r', encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="fdsreader",
    use_incremental=True,
    setup_requires=['incremental'],
    author="FZJ IAS-7 (Prof. Dr. Lukas Arnold, Jan Vogelsang)",
    author_email="j.vogelsang@fz-juelich.de",
    description="Python reader for data generated by FDS.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FireDynamics/fdsreader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'incremental',
        'numpy',
        'typing_extensions'
    ],
)
