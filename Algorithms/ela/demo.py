#!/usr/bin/env python

#Import all the packages useful for the Demo.
import argparse
from PIL import Image
from analyse import *

"""Define a parser to parse the arguments given to the program."""
parser = argparse.ArgumentParser(description="Image Forensics")

""" One can specify in the command line of the program either -o or --origin (it will be the same to specify -o or --origin) + name of the original image. This is optional argument. If the user specify it, he can specify the path of his own original image."""
parser.add_argument("-o", "--origin", default='../../images/set1/forensicsOrigin.jpg', help='name of the original image file')

""" One can specify in the command line of the program either -t or --tmp (it will be the same to specify -t or --tmp) + name of the tampered image. This is optional argument. If the user specify it, he can specify the path of his own tampered image."""
parser.add_argument("-t", "--tmp", default='../../images/set1/forensicsTmp.jpg', help='name of the tampered image file')

""" One can specify in the command line of the program either -c or --convertGreyScale (it will be the same to specify -c or --convertGreyScale). This is optional argument. If the user specify it, args.convertGreyScale == True, else args.convertGreyScale == False)"""
parser.add_argument("-c", "--convertGreyScale", help="The image is converted to grayscale if specified", action="store_true")

"""Parse the arguments given to the program."""
args = parser.parse_args()

# Perform the forensic analysis and show the results.
OutputMap = analyze(args.origin, args.tmp, args.convertGreyScale);
OutputMap.show()
