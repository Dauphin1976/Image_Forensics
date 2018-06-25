#!/usr/bin/env python

#Import all the packages useful for the module.
from ela import *

# Perform the forensic analysis.
def analyze(ImOriginal, ImTmp, convertGreyScale):

	# Perform ELA (Error Level Analysis) forensic analysis.
    OutputMap = ELA(ImOriginal, ImTmp, convertGreyScale)

	# Return results.
    return OutputMap
