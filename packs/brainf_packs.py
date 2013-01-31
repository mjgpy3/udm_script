#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 16:47:44 EST 2013
# 
# 

from package_container import PackageContainer

packages = {}

special_package_instructions = {'brainf': 
                                    ['wget wget https://raw.github.com/mjgpy3/Brainf___Interpreter/master/brainfint.py',
                                     'mv brainfint.py /bin/brainf',
                                     'chmod 777 /bin/brainf']}

container = PackageContainer("BrainF***", None, packages, special_package_instructions)
