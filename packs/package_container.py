#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 16:35:35 EST 2013
# 
# 

from os import system

class PackageContainer:
    """
        Holds the information for a package and associated, sort
        of, "sub-packages"
    """

    def __init__(self, name, its_package, packages={}):
        self.name = name
        self.package = its_package
        self.packages = packages

    def install_me(self):
        """
            Installs the package and it's "sub-packages"
        """
        
        failed_packs = []

        if self.package:
            if self.run_install_on(self.package) != 0:
                failed_packs.append(self.package)

        for package in self.packages.values():
            if self.run_install_on(package) != 0:
                failed_packs.append(package)

        return failed_packs

    def run_install_on(self, package):
        """
            Runs an install command on the passed package name
        """

        # Not very dynamic, but...
        return system('yes | apt-get install ' + package)

