"""The script reads the parameters from the random toolbox by creating an empty inlist. The random empty list is filled in with randomly selected values from inlist."""


import arcpy    #imports arcpy 
import random
from arcpy import env    #sets workspace environment
env.overwriteoutput =  True     #Overwrites copies of wriiten programme already run
inputfc = arcpy.GetParameterAsText(0)         #Sets paramters for workspace: input file, output file and count of the feature
outputfc = arcpy.GetParameterAsText(1)
outcount = int(arcpy.GetParameterAsText(2))
desc = arcpy.Describe(inputfc)    #Gives description of input file
inlist = []                      #primes empty lists to be filled
randomlist = []
fldname = desc.OIDFieldName
rows = arcpy.SearchCursor(inputfc)
row = rows.next()
while row:                            #sets conditions for filling in empty lists with random features.
    id = row.getValue(fldname)
    inlist.append(id)
    row = rows.next()
while len(randomlist) < outcount:
    selitem = random.choice(inlist)
    randomlist.append(selitem)
    inlist.remove(selitem)
length = len(str(randomlist))        #sets length of the random list generated
sqlexp = '"' + fldname + '"' + " in " + "(" + str(randomlist)[1:length - 1] + ")"     #SQL expression for concatenation of fields with random lists
arcpy.MakeFeatureLayer_management(inputfc, "selection", sqlexp)
arcpy.CopyFeatures_management("selection", outputfc)                                   #Output for selected features
