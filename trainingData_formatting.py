import os
import arcpy
from arcpy import management

os.chdir(r'C:\Users\mleung\Desktop\sanDiego\classifications') #change to file path for your classifications
os.listdir()

# Extract by Mask for sites likes British Columbia
os.chdir(r'C:\Users\mleung\Desktop\britishColumbia\classifications')

ExtractByMask('20201107_185022_97_222f_3B_AnalyticMS_SR_8b_harmonized_clip.tif', 
              os.chdir(r'20201107_185022_97_222f_3B_AnalyticMS_SR_8b_harmonized_clip.tif'), 
              {extraction_area}, 
              {analysis_extent})

# for loop to automate Extract by Mask tool
ExtractByMask(in_raster, 
              in_mask_data, 
              {extraction_area}, 
              {analysis_extent})

# sets current directory through arcpy instead of os package
arcpy.env.workspace = "C:/Users/mleung/Desktop/sanDiego/classifications"

walk = arcpy.da.Walk(datatype="RasterDataset")

for dir_path, dir_names, file_names in walk:
    for filename in file_names:
        print(os.path.join(dir_path, filename))

fileList = arcpy.ListFiles("*.tif")
print(fileList)

# lists files and stores them 
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

# for loop to automate Copy Raster tool
for raster in os.listdir(r'C:\Users\mleung\Desktop\santaBarbara\classifications_noAux'): #change file path
    if raster.endswith('.tif'):
        outRaster = raster.replace('.tif', '_final.tif')
        arcpy.management.CopyRaster(raster,
                                   outRaster,
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
