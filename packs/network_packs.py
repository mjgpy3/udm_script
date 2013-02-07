#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 16:47:44 EST 2013
# 
# 

from package_container import PackageContainer

packages = {'Nmap': 'nmap',
            'Wireshark': 'wireshark'}

container = PackageContainer("Network Tools", None, packages)
