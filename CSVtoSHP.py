#-------------------------------------------------------------------------------
# Name:        CSV to SHP
# Purpose:
#
# Author:      James.Runnalls
#
# Created:     10/02/2016
# Copyright:   (c) James.Runnalls 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Import relevant modules
import arcpy, csv, math, time, sys
import Tkinter as t
import tkFileDialog as tf
import tkMessageBox as tm
import os
import xml.etree.ElementTree as ET

outputfiles = r"C:\Users\James.Runnalls\Desktop\PR19"

outputCSV = '{0}.csv'.format(outputfiles)
outputLYR = '{0}.lyr'.format(outputfiles)
outputLYR = outputLYR.replace('/','\\')
outputSHP = '{0}.shp'.format(outputfiles)
outputSHP = outputSHP.replace('/','\\')

# Set coordinate system
spRef = r"Coordinate Systems\Projected Coordinate Systems\National Grids\Europe\British National Grid.prj"

# Populate shapefile
arcpy.MakeXYEventLayer_management(outputCSV,'xcoord','ycoord',outputLYR,spRef)

# Save to a layer file
arcpy.CopyFeatures_management(outputLYR, outputSHP)