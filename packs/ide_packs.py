#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 17:51:03 EST 2013
# 
# 

from package_container import PackageContainer

packages = {'Eclipse': 'eclipse',
            'Eclipse C/C++': 'eclipse-cdt',
            'MonoDevelop': 'monodevelop',
            'Mono Python': 'monodevelop-python',
            'Mono Java': 'monodevelop-java',
            'Mono Vala': 'monodevelop-vala',
            'Netbeans': 'netbeans',
            'Gedit': 'gedit',
            'Jedit': 'jedit',
            'VIM': 'vim',
            'BlueFish': 'bluefish',
            'Geany': 'geany',
            'Komposer': 'kompozer',
            'Anjuta': 'anjuta',
            'Glade': 'glade',
            'Code::Blocks': 'codeblocks',
            'Arduino': 'arduino',
            'Emacs': 'emacs'}

container = PackageContainer("IDEs", None, packages)

