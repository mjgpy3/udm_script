#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 17:20:17 EST 2013
# 
# 

import packs
from os import system

def install_desired_packs():
    """
        Loops through the desired containers and installs them
    """

    failed_packs = []

    for container in packs.desired_packages.package_containers:
        failed_packs += container.install_me()

    if failed_packs != []:
        print "\nThe following packages failed to install correctly:"
        print "\n".join(pack_name for pack_name in failed_packs)
    else:
        print "\nEverything installed correctly"

def get_string_name_and_pack(name, pack):
    return name + (' (' + pack + ')' if pack != None else '') + '\n'

def get_string_of_packages():
    """
        Returns a string of all packages that ought to be
        installed
    """
    packages = ''
    for container in packs.desired_packages.package_containers:
        packages += get_string_name_and_pack(container.name, container.package)
        for name in container.packages:
            packages += '-> ' + get_string_name_and_pack(name,
                                                        container.packages[name])
    return packages
    

def prompter():
    """
        Asks the user whether they want to install the software
        or not
    """
    
    system('echo "' + get_string_of_packages() +'" | less')

    return raw_input("Install the listed software? (yes/no): ").lower().startswith('y')

if __name__ == '__main__':
    if prompter():
        install_desired_packs()
