from setuptools import setup
import os
import re

def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

with open("README.rst", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

version = get_version('python_package_demo')


setup(
    name='python-package-demo',
    version='0.1.0',
    packages=['python_package_demo'],
    description='Example package setup for INEOS python repository',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url= "H:/Python/python-package-demo",
    author='Kevin Jaggs',
    license='MIT',
    author_email='kevin.jaggs@ineos.com',
    install_requires=[required],
    keywords='python git setup example',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
