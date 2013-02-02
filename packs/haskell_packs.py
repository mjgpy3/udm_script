#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 16:47:44 EST 2013
# 
# 

from package_container import PackageContainer

packages = {'Cabal': 'cabal-install',
            'Haskell Platform': 'haskell-platform'}

container = PackageContainer("Haskell", 'ghc', packages)
