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


Notes:
------


>Input classes are processed using numpy.select. This means that in many cases, consecutive ranges should be defined using "<" rather than ">" to avoid classes over-riding each other.  For example "> 0, > 2, > 4" will produce one class that is greater than 4 trumping the first two conditions, whereas "< 3, < 5, < 10" will produce 3 classes.

>Thanks to Chris Garrard for providing such great Python GDAL tutorials: http://www.gis.usu.edu/~chrisg/
