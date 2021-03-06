"""
lambdata - a collection of Data Science helper functions
"""

import setuptools
REQUIRED = [
    "numpy", 
    "pandas"
]

with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()

setuptools.setup(
    name = "lambdata-bbrauser",
    version = "0.0.8",
    author = "bbrauser", 
    description = "A collection of Data Science helper functions", 
    long_description = LONG_DESCRIPTION, 
    long_description_content_type = "text/markdown", 
    url = "https://github.com/bbrauser/lambdata", 
    packages = setuptools.find_packages(), 
    python_requires = ">=3.6", 
    install_requires = REQUIRED, 
    classifiers = [
        "Programming Language :: Python :: 3", 
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent", 
    ],
)
