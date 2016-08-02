'''A module for testing heatmap and barplot classes sing py.test framework.
    Specify path to input data file, and path to output png file for both functions'''

from plotmaker_poly import HeatMapMaker, BarPlotMaker
import os.path

def test_plotmakerHM_exist():

    myobj = HeatMapMaker("C:/Users/rharihar/Desktop/Heatmapdata.csv",
                         "C:/Users/rharihar/Desktop/heatmap_1.png")
    myobj.plotmaker()
    x = os.path.exists("C:/Users/rharihar/Desktop/heatmap_1.png")
    assert x == True
    
def test_plotmakerBPM_exist():
    myobj = BarPlotMaker("C:/Users/rharihar/Desktop/Barplotdata.csv",
                         "C:/Users/rharihar/Desktop/Barplot_1.png")
    myobj.plotmaker()
    x = os.path.exists("C:/Users/rharihar/Desktop/Barplot_1.png")
    assert x == True

    
