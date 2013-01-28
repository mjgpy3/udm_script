#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 17:51:03 EST 2013
# 
# 

from package_container import PackageContainer

packages = {'Eclipse': 'eclipse',
            'Eclipse C/C++': 'eclipse-cdt',
            'MonoDevelop': 'monodevelop',
            'Mono Game': 'monodevelop-monogame',
            'Netbeans': 'netbeans',
            'Gedit': 'gedit',
            'Jedit': 'jedit',
            'VIM': 'vim',
            'BlueFish': 'bluefish',
            'Geany': 'geany',
            'Anjuta': 'anjuta',
            'Glade': 'glade-gtk2',
            'Code::Blocks': 'codeblocks',
            'Arduino': 'arduino',
            'Emacs': 'emacs',
            'Leksah': 'leksah'}

container = PackageContainer("IDEs", None, packages)

