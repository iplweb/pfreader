#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

def reqs(fn):
    return list([x.strip()
                 for x in open(fn).readlines()
                 if
                 x.strip()
                 and not x.startswith("-")
                 and not x.startswith("\#")])

requirements = reqs("requirements.txt")
test_requirements = reqs("requirements_dev.txt")

setup(
    name='pfreader',
    version='0.0.4-dev',
    description="Reader for Baxter® PrismaFlex® LOX files",
    long_description=readme + '\n\n' + history,
    author="IPLWeb",
    author_email='michal.dtz@gmail.com',
    url='https://github.com/mpasternak/pfreader',
    packages=[
        'pfreader',
    ],
    package_dir={'pfreader': 'src/pfreader'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=True,
    keywords='PrismaFlex Baxter Prisma Flex Gambro LOX files CRRT CVVHDF TPE',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
