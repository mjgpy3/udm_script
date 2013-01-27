#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 16:47:44 EST 2013
# 
# 

from package_container import PackageContainer

packages = {'Git': 'git',
            'SVN': 'subversion',
            'CVS': 'cvs',
            'Mercurial': 'mercurial',
            'Mono Version Control': 'monodevelop-versioncontrol'}

container = PackageContainer("Source Control", None, packages)
