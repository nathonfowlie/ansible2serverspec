####################################################################################################
# Copyright 2017 Nathon Fowlie
#
# Licensed under the Apache License, Version 2.0(the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
#
# http: // www.apache.org / licenses / LICENSE - 2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.
####################################################################################################


from setuptools import setup, find_packages
import sys, os

def readme():
    with open('README') as f:
        return f.read()

setup(name='ansible2serverspec',
    version='1.0',
    description="Exports Ansible variable dictionaries to Yaml format.",
    long_description=readme(),
    classifiers=[
        "Topic :: System :: Systems Administration",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: System Administrators",
    ],
    author='Nathon Fowlie',
    author_email='nathon.fowlie@gmail.com',
    url='https://github.com/nathonfowlie/ansible2serverspec',
    license='Apache Software License, Version 2.0',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    keywords = 'ansible serverspec yaml',
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=[
        ### Required to build documentation
        # "Sphinx >= 1.0",
        ### Required for testing
        # "nose",
        # "coverage",
        ### Required to function
        'cement',
        'ansible',
        'ruamel.yaml',
        'colorama',
        'argparse',
        ],
    setup_requires=[],
    entry_points="""
        [console_scripts]
        ansible2serverspec = ansible2serverspec.cli.main:main
    """,
    namespace_packages=[],
    )
