#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 16:47:44 EST 2013
# 
# 

from package_container import PackageContainer

packages = {'Cabal': 'cabal-install',
            'Haskell Platform': 'haskell-platform',
            'Drift': 'drift',
            'Hugs': 'hugs',
            'lhs2Tex': 'lhs2tex',
            'HLint': 'hlint'}

special_packs = {'Haddock': ['cabal update', 'cabal install haddock'],
                 'HUnut': ['cabal update', 'cabal install hunit'],
                 'Vacuum': ['cabal update', 'cabal install vacuum'],
                 'Virthualenv': ['cabal update', 'cabal install virthualenv'],
                 'QuickCheck': ['cabal update', 'cabal install quickcheck'],
                 'Hoogle': ['cabal update', 'cable install hoogle'],
                 'Stylish Haskell': ['cabal update', 'cabal install stylish-haskell'],
                 'Source Graph': ['cabal update', 'cabal install sourcegraph']}

container = PackageContainer("Haskell", 'ghc', packages)
