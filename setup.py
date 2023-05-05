import os
import subprocess

import setuptools

with open("README.md", "r") as readme:
    readme = readme.read()

with open("requirements.txt", "r") as requirements:
    requirements = requirements.read()

setuptools.setup(
    name="depraved",
    version=0.1,
    author="Joseph Torsney",
    author_email="jetorsney1@sheffield.ac.uk",
    description="dePRAVEd: a Phoneme Realtime Audio Variational autoEncoder",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_data={
        'rave/configs': ['*.gin'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": [
        "depraved = scripts.main_cli:main",
    ]},
    install_requires=requirements.split("\n"),
    python_requires='>=3.9',
    include_package_data=True,
)
