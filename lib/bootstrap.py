# -*- coding: utf-8 -*-
#
# Author: Cayetano Benavent, 2014.


from gdalreclassify import GdalReclassify

"""
src_file: source file

dst_file: destination file

in_classes: values to be reclassified

out_classes: The number of input classes must match the number of result values. The order of the output classes must match the order of the input classes.

output_format: Output GDAL format

default: Value used to fill pixels that do not meet any conditions of the input classes. If this value is not specified, the default will be 0.

nodata: Setting to 'True' sets the default value as the nodata value.

compress_type: 'COMPRESS = LZW','COMPRESS = PACKBITS','COMPRESS = DEFLATE','COMPRESS = JPEG'. The default is no compression.
"""


src_file = 'source_rasterfile.tif'
dst_file = 'destination_rasterfile.tif'
in_classes = ['<-64.0', '<-60.0', '<-56.0', '<-52.0', '<-48.0', '<-44.0', '<-40.0', '<100.0']
out_classes = ['1', '2', '3', '4', '5', '6', '7', '8']

gr = GdalReclassify(src_file, dst_file)
gr.processDataset(in_classes, out_classes, default=False, nodata=[], output_format='GTiff', compress_type=['COMPRESS=None'])
    
