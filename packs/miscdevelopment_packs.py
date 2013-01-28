#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 16:47:44 EST 2013
# 
# 

from package_container import PackageContainer

packages = {'make': 'make',
            'Apache2': 'apache2',
            'Sqlite Browser': 'sqlitebrowser',
            'Gitg': 'gitg',
            'Natural Docs': 'naturaldocs',
            'VDKbuilder': 'vdkbuilder2',
            'Terminator': 'terminator',
            'Guake': 'guake',
            'ReText': 'retext',
            'XTerm': 'xterm'}

container = PackageContainer("Misc", None, packages)
