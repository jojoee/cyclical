import pathlib
from setuptools import setup, find_packages

# https://stackoverflow.com/questions/14399534/reference-requirements-txt-for-the-install-requires-kwarg-in-setuptools-setup-py
requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cyclical",
    version="1.0.2",
    description="Encode item list into cyclical",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jojoee/cyclical",
    author="Nathachai Thongniran",
    author_email="inid3a@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=requirements,
    keywords=["cyclical", "cyclic", "normalization", "normalize"],
)
