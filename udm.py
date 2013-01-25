#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 17:20:17 EST 2013
# 
# 

import packs

def install_desired_packs():
    for container in packs.desired_packages.package_containers:
        container.install_me()

if __name__ == '__main__':
    install_desired_packs()
