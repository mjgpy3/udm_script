#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 17:51:03 EST 2013
# 
# 

from package_container import PackageContainer

packages = {'JRuby': 'jruby'}

special_instructions = {'JSON': ['gem install json']}

container = PackageContainer("Ruby", 'ruby', packages, special_instructions)

