#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 16:47:44 EST 2013
# 
# 

from package_container import PackageContainer

packages = {'Cabal': 'cabal-install',
            'Haskell Platform': 'haskell-platform',
            'Drift': 'drift',
            'Hugs': 'hugs'}

special_packs = {'Haddock': ['cabal update', 'cabal install haddock']}

container = PackageContainer("Haskell", 'ghc', packages)
