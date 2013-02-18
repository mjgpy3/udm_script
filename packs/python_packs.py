#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 16:47:44 EST 2013
# 
# 

from package_container import PackageContainer

packages = {'Pygame': 'python-pygame',
            'Sympy': 'python-sympy', 
            'Numpy': 'python-numpy',
            'Scipy': 'python-scipy',
            'Virtualenv': 'python-virtualenv',
            'PIP': 'python-pip',
            'Django': 'python-django',
            'Pychecker': 'pychecker',
            'IPython': 'ipython',
            'IDLE': 'idle',
            'Epydoc': 'python-epydoc',
            'Sphinx': 'python-sphinx',
            'SQLAlchemy': 'python-sqlalchemy',
            'Requests': 'python-requests',
            'Flask': 'python-flask',
            'Python Dev': 'python-dev',
            'Beautiful Soup': 'python-beautifulsoup',
            'Jython': 'jython',
            'Cython': 'cython',
            'PyPy': 'pypy',
            'Python Openoffice': 'python-openoffice'}

special_package_instructions = {'sh': ['pip install sh']}


container = PackageContainer("Python", 'python', packages, special_package_instructions)
