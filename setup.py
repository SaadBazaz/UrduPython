# References:
# - https://stackoverflow.com/questions/27494758/how-do-i-make-a-python-script-executable

from setuptools import setup, find_packages

files = ["samples/*/*", "languages/*/*.yaml"]

setup(
    name='urdupython',
    version='0.0.8',
    author='Saad Bazaz',
    author_email='saadbazaz@hotmail.com',
    url='https://github.com/saadbazaz/UrduPython',
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