import setuptools
from setuptools import setup

import mintchoco

setup(
    name="mintchoco",
    version=mintchoco.__version__,
    author="Ryu JuHeon",
    author_email="SaidBySolo@gmail.com",
    url="https://github.com/Saebasol/Mintchoco",
    description="Heliotrope python wrapper",
    long_description=open("README.md", "rt", encoding="UTF8").read(),
    long_description_content_type="text/markdown",
    license="MIT License",
    packages=setuptools.find_packages(),
    package_data={"mintchoco": ["py.typed"]},
)
