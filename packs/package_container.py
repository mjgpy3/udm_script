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

    def __init__(self, name, its_package, packages={}, spc = None):
        self.name = name
        self.package = its_package
        self.packages = packages
        self.special_instructions = spc

    def install_me(self):
        """
            Installs the package and it's "sub-packages"
        """
        
        failed_packs = []

        # If this container specifies a package, install it
        if self.package:
            if self.run_install_on(self.package) != 0:
                failed_packs.append(self.package)

        # If this container specifies multiple package, install them
        for package in self.packages.values():
            if self.run_install_on(package) != 0:
                failed_packs.append(package)

        # If this container has any special installation instructions, run them
        if self.special_instructions:
            for tool in self.special_instructions:
                for instruction in self.special_instructions[tool]:
                    if system(instruction) != 0:
                        failed_packs.append(tool)
                        continue

        return failed_packs

    def run_install_on(self, package):
        """
            Runs an install command on the passed package name
        """

        # Not very dynamic, but we'll let `self.special_instructions`
        # handle anything non-`apt-get install ...`
        return system('yes | apt-get install ' + package)

