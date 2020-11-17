# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:34:22 2020

@author: mysh
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Hyperion-Stemonitis", # Replace with your own username
    version="0.0.1",
    author="Anastasia Tokhtamysh",
    author_email="atokhtamysh@gmail.com",
    description="Tool for reading, preprocessing and analysing Hyperion Earth Observer-1 (EO-1) data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Stemonitis/Hyperion",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)