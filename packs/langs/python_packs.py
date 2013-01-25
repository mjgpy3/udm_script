#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 16:47:44 EST 2013
# 
# 

import sys
sys.path.append('..')

from package_container import PackageContainer


packages = {'Pygame': 'python-pygame',
            'Sympy': 'python-sympy', 
            'Numpy': 'python-numpy',
            'Scipy': 'python-scipy',
            'Virtualenv': 'python-virtualenv',
            'PIP': 'python-pip'}

container = PackageContainer("Python", 'python', packages)
