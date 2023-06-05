# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="ITM TA3 MVP API",
    author_email="",
    url="",
    keywords=["Swagger", "ITM TA3 MVP API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    This is the specification of a proposed TA3 API for the In The Moment (ITM) Minimum Viable Product (MVP).  It is based on the OpenAPI 3.0 specification.  Some objects and operations are not necessarily planned for the MVP, but are currently present for fostering discussion.  The API is currently in an draft state, even in the context of an MVP.
    """
)
