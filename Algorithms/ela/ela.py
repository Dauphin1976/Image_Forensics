#!/usr/bin/env python

#Import all the packages useful for the module.
from PIL import Image, ImageChops

# Compute Error Level Analysis of two images.
def ELA(ImOriginal, ImTmp, convertGreyScale):
    
    # Open the original image and the tampered image.
    original = Image.open(ImOriginal)
    temporary = Image.open(ImTmp)

	# Compute Error Level Analysis.
    OutputMap = ImageChops.difference(original, temporary)
    
    # If convertGreyScale is set to true, then convert the resulting image in greyscale.
    if convertGreyScale: 
        OutputMap = OutputMap.convert('LA')

	# Return results.
    return OutputMap
