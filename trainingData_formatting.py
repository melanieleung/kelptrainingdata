import os
import arcpy
from arcpy import management
from arcpy import sa

## EXTRACT BY MASK : WIP ##
arcpy.env.workspace = "C:/Users/mleung/Desktop/britishColumbia/classifications" # file path for classifications
classList = arcpy.ListFiles("*.tif")
arcpy.env.workspace = "C:/Users/mleung/Desktop/britishColumbia/imagery" # file path for imagery
imageList = arcpy.ListFiles("*.tif")

for raster in classList:
    fileName = os.path.splitext(raster)[0]
    # define the output file
    rastFile = raster + "_extracted.tif"
    # run the copy raster tool
    arcpy.sa.ExtractByMask(classList, #input raster
                           imageList, #mask raster
                           rastFile)  #output raster

# sets current directory through arcpy instead of os package
arcpy.env.workspace = "C:/Users/mleung/Desktop/trainingData_planet8band/monterey/rerun/finalOutputs"

walk = arcpy.da.Walk(datatype="RasterDataset")

for dir_path, dir_names, file_names in walk:
    for filename in file_names:
        print(os.path.join(dir_path, filename))

fileList = arcpy.ListFiles("*.tif")
print(fileList)

## COPY RASTER ##
fileList = arcpy.ListFiles("*.tif")

for raster in arcpy.ListFiles("*.tif"):
    # get the file name without extension (replaces the %Name% variable from ModelBuidler)
    fileName = os.path.splitext(raster)[0]
    # define the output file
    rastFile = fileName + "_final.tif" 
    # run the copy raster tool
    arcpy.management.CopyRaster(raster,
                                rastFile,
                                '', 
                                '',
                                3,
                                'NONE',
                                'NONE',
                                '8_BIT_UNSIGNED',
                                'NONE',
                                'NONE', # color map to RGB
                                'TIFF',
                                'NONE',
                                'CURRENT_SLICE',
                                'NO_TRANSPOSE')
