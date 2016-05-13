#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="xstools",
    version="0.1.0",
    packages=find_packages('xstools'),
    package_dir={'': 'xstools'},
    zip_safe=False,

    description="xinshi's tools.",
    long_description=u"这是我的工具",
    author="xinshi",
    author_email="xinshihsnix@sina.cn",

    license="GPL",
    keywords=("xstools", "egg"),
    platforms="Independant",
    url="",
)