#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 16:45:15 EST 2013
# 
# 

"""
    Simply contains a list of all the package containers that will be
    installed
"""

import c_packs
import csharp_packs
import erlang_packs
import fortran_packs
import haskell_packs
import ide_packs
import java_packs
import latex_packs
import python_packs
import r_packs
import ruby_packs
import scala_packs
import smalltalk_packs
import source_control_packs

package_containers = [c_packs.container,
                      csharp_packs.container,
                      erlang_packs.container,
                      fortran_packs.container,
                      haskell_packs.container,
                      ide_packs.container,
                      java_packs.container,
                      latex_packs.container,
                      python_packs.container,
                      r_packs.container,
                      ruby_packs.container,
                      scala_packs.container,
                      smalltalk_packs.container,
                      source_control_packs.container]
