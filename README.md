# Polymorphic-OO-plotmaker
A polymorphic data plotter written in Python 3, and it includes basic tests in py.test framework.

The module plotmaker_poly.py contains one base class, DataReader, whose __init__ function also opens and reads in a csv file as a pandas dataframe. There are two subclasses, class HeatMapMaker which plots a heat map, and class BarPlotMaker, which makes a barplot. Both subclasses inherit DataReader class. They both have the plotmaker method, but act on different data.

The module plotmaker_master.py contains the factory method plotmaker_master that controls the behaviour of the plotmaker_poly.py module. If input data file name contains the word "Heatmap", it instantiates the plotmaker method under the HeatMapMaker subclass. However, if the input file name contains the word "Barplot", it instantiates the plotmaker method under the BarPlotMaker subclass.

The test_plotmaker_poly contains unit tests for the HeatMapMaker, and BarPlotMaker subclasses, and uses py.test unit testing framework. Also included are two sample data files for barplot and heatmap.

There is scope to improve the code, and this will be updated in future. This is just sample code to drive home the concept of polymorphism, and its functionality, at the moment, is trivial. 
