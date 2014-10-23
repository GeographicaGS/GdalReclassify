Description
============

Library to reclassify raster data using GDAL.

Based on the command line utility gdal_reclasify.py 
developed by Cyrus Hiatt:
https://github.com/chiatt/gdal_reclassify

Requirements
=============

* python
* numpy
* gdal binaries
* python-gdal bindings

Usage
=======

bootstrap.py

```
src_file = 'source_rasterfile.tif'
dst_file = 'destination_rasterfile.tif'
in_classes = ['<-64.0', '<-60.0', '<-56.0', '<-52.0', '<-48.0', '<-44.0', '<-40.0', '<100.0']
out_classes = ['1', '2', '3', '4', '5', '6', '7', '8']

gr = GdalReclassify(src_file, dst_file)
gr.processDataset(in_classes, out_classes, default=False, nodata=[], output_format='GTiff', compress_type=['COMPRESS=None'])
```


Notes:
------


>Input classes are processed using numpy.select. This means that in many cases, consecutive ranges should be defined using "<" rather than ">" to avoid classes over-riding each other.  For example "> 0, > 2, > 4" will produce one class that is greater than 4 trumping the first two conditions, whereas "< 3, < 5, < 10" will produce 3 classes.

>Thanks to Chris Garrard for providing such great Python GDAL tutorials: http://www.gis.usu.edu/~chrisg/
