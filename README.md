# kelptrainingdata
Scripts for automating processing and formatting training data of classified PlanetScope 8 band imagery of kelp

Mostly for loops of the most commonly used Arc tools for this process such as: Extract by Mask, Copy Raster, and Reclassify. 
Best if used through the Python module in ArcGIS Pro.
Training data classifications are intended to be the inputs of the tools in this script and the expected outputs are 8bit unsigned, 1 band, rasters consisting
of a NoData value of 3 and displaying 3 classes: 0s for water, 1s for kelp, and 2s for land.
