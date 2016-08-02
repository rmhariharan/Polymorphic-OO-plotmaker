from plotmaker_poly import HeatMapMaker,BarPlotMaker

def plotmaker_master(infile,outfile):
    if infile.find("Heatmap") != -1:
        plotobj = HeatMapMaker(infile,outfile)
        plotobj.plotmaker()
    elif infile.startswith("Barplot") != -1:
        plotobj = BarPlotMaker(infile,outfile)
        plotobj.plotmaker()
    return "Plot making complete"
