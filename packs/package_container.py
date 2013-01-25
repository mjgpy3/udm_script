#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 16:35:35 EST 2013
# 
# 

class PackageContainer:
    def __init__(self, name, its_package, packages={}):
        self.name = name
        self.package = its_package
        self.packages = packages

    def install_name_and_packages(self):
        pass
