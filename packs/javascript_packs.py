#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 16:47:44 EST 2013
# 
# 

from package_container import PackageContainer

packages = {'Node.js': 'nodejs',
            'CoffeeScript': 'coffeescript',
            'Node Package Manager': 'npm'}

container = PackageContainer("JavaScript", 'rhino', packages)
