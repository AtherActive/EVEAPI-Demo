# EVEPy - EVE Online Library for Python
# Copyright (C) 2020 - AtherActive
# View terms in LICENSE.txt file.
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EVEPy-saltylelele", 
    version="0.0.1",
    author="Julian G",
    author_email="iamsalt@atheractive.net",
    description="A Python library for the EVE Online API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atheractive/evepy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)