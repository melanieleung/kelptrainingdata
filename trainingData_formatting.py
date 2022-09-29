import os
import arcpy
from arcpy import management

os.chdir(r'C:\Users\mleung\Desktop\santaBarbara\classifications') #change to file path for your classifications
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

# for loop to automate Copy Raster tool
for raster in os.listdir(r'C:\Users\mleung\Desktop\santaBarbara\classifications'): #change file path
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

arcpy.ValidateFieldName('20200827_175133_89_222c_3B_AnalyticMS_SR_8b_harmonized_clip.tif')

arcpy.management.CopyRaster('20200827_175133_89_222c_3B_AnalyticMS_SR_8b_harmonized_clip.tif',
                                   '20200827_175133_89_222c_3B_AnalyticMS_SR_8b_harmonized_clip_final.tif',
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
