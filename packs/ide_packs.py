#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 17:51:03 EST 2013
# 
# 

from package_container import PackageContainer

packages = {'Eclipse': 'eclipse',
            'Eclipse C/C++': 'eclipse-cdt',
            'MonoDevelop': 'monodevelop',
            'NUnit (mono)': 'monodevelop-nunit',
            'Netbeans': 'netbeans',
            'Gedit': 'gedit',
            'Gedit Plugins': 'gedit-plugins',
            'Jedit': 'jedit',
            'VIM': 'vim',
            'VIM GTK': 'vim',
            'VIM Rails': 'vim-rails',
            'VIM LaTeX': 'vim-latexsuite',
            'BlueFish': 'bluefish',
            'Geany': 'geany',
            'Anjuta': 'anjuta',
            'Glade': 'glade-gtk2',
            'Code::Blocks': 'codeblocks',
            'Arduino': 'arduino',
            'Emacs': 'emacs',
            'Leksah': 'leksah',
            'Codelite': 'codelite',
            'LyX': 'lyx',
            'Abiword': 'abiword',
            'Kate': 'kate',
            'PyRoom': 'pyroom',
            'DRPython': 'drpython',
            'PIDA': 'pida',
            'Spyder': 'spyder',
            'Eric': 'eric',
            'E3': 'e3',
            'CSS Editor': 'cssed',
            'TexMaker': 'texmaker'}

container = PackageContainer("IDEs", None, packages)

