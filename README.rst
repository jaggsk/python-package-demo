Python Package Demo
-------------------

A demonstration of how to set up a git repo on the INEOS system - intended to provoke discusion on python scripting best practice.

Below is a first pass proposal for storing python scripts in a centralised location and with the functionality for any user to install as a local python package.

Author: K Jaggs kevin.jaggs@ineos.com


Python Package Structure
------------------------

.. code:: bash

    python-package-demo/
    |
    ├── setup.py
    ├── README.md
    ├── requirements.txt
    |
    ├── python_package_demo/
      ├── goodbye.py
      ├── hello.py
      ├── __init__.py


Installation
------------

Installation can be directly from the file location or from a git repo.

Find the path of your main Python installation - the package will be installed to the site-packages directory in this location.

.. code:: bash

    which python

.. code:: bash

    C:\Users\kxj17699\AppData\Local\Programs\Python\Python311\Lib\site-packages

Install the package from a new cmd window (ensure not in the active venv) using the following command. python -m ensures that the main python installation is used and not an associated  virtual environment. 

.. code:: bash

    python -m pip install "H:/Python/python-package-demo"

Install directly from a local git repo - best practice?

.. code:: bash

    pip install git+https://github.com/jaggsk/python-package-demo

Programming using Virtual Environments
--------------------------------------


"Python virtual environments create isolated contexts to keep dependencies required by different projects separate so they don't interfere with other projects or system-wide packages. Basically, setting up virtual environments is the best way to isolate different Python projects, especially if these projects have different and conflicting dependencies. As a piece of advice for new Python programmers, always set up a separate virtual environment for each Python project, and install all the required dependencies inside it — never install packages globally."

.. code:: python

    #Setting up a vitual environment
    #Navigate to root directory and run the following command
    
    python -m venv venv

    #Activate the vitrual environament with the following
    
    venv\Scripts\activate

    #Run VS Code from the venv. Explorer window is referenced to root directory
    
    code .

    #deactivate venv session
    
    deactivate


README file
-----------

A README file should convey the following information.

- What the project does
- Why the project is useful
- How users can get started with the project
- Where users can get help with your project
- Who maintains and contributes to the project

Making a README file using rst format
-------------------------------------

Quick fix - install the following extension from vs code marketplace:

https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext&ssr=false#qna


You will also need to install pygments to view bash and code snippets

.. code:: python

    pip install pygments

Save a README.rst file and start typing some text.
To view the preview pane press ctrl-shift-k-v. When you save the .rst file the preview is automatically updated.

__init__ file
-------------

"The __init__.py file lets the Python interpreter know that a directory contains code for a Python module. An __init__.py file can be blank. Without one, you cannot import modules from another folder into your project."

In our example we have a reference to the the version ID __version__ and explicit import commands to the required .py files.

.. code:: python

    from python_package_demo.hello import say_hello
    from python_package_demo.goodbye import say_goodbye

    __version__ = "1.0.1"


requirements.txt
----------------

The requirements file provides the necessary downloads and version numbers required for the installation.

requirements.txt is created using the following command within the active venv environment.

.. code:: bash

    pip freeze > requirements.txt

    docutils==0.20.1
    numpy==1.25.1
    plumbum==1.8.2
    ply==3.11
    Pygments==2.15.1
    pywin32==306



setup.py
--------

Setup file installs the python_package_demo folder as global python package.

Version number, readme file and requirements.txt are read to the installation. 

Version number standards are found here: https://peps.python.org/pep-0440/

.. code:: python

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
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ], # Get classifiers from http://pypi.python.org/pypi?%
    )
