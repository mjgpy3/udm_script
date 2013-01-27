#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 16:45:15 EST 2013
# 
# 

"""
    Simply contains a list of all the package containers that will be
    installed
"""

import python_packs
import haskell_packs
import source_control_packs
import ide_packs
import smalltalk_packs

package_containers = [python_packs.container,
                      haskell_packs.container,
                      smalltalk_packs.container,
                      source_control_packs.container,
                      ide_packs.container]
