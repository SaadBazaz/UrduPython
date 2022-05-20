# References:
# - https://stackoverflow.com/questions/27494758/how-do-i-make-a-python-script-executable

import os
from setuptools import setup, find_packages

files = ["samples/*/*", "languages/*/*.yaml"]

with open('requirements.txt') as f:
    required_versions = f.read().splitlines()
    required = []
    for required_package in required_versions:
        print ("Package:", required_package.split("==")[0])
        required.append(required_package.split("==")[0])
        
setup(
    name='urdupython',
    version='0.1.3',
    author='Saad Bazaz',
    author_email='saadbazaz@hotmail.com',
    url='https://github.com/saadbazaz/UrduPython',

    install_requires=required,
    # packages=['urdupython', 'modes', 'filters', 'languages'],
    packages=find_packages(),
    package_data = {'urdupython' : files },

    entry_points={
        'console_scripts': [
            'urdupython=urdupython.urdu_python:main',
            'اردوپایتھان=urdupython.urdu_python:main',
            'اردوپای=urdupython.urdu_python:main'
        ]
    }
)
