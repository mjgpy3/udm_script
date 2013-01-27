#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 16:47:44 EST 2013
# 
# 

from package_container import PackageContainer

packages = {'Sqlite': 'sqlite',
            'MySql Server': 'mysql-server'}

container = PackageContainer("SQL", None, packages)
