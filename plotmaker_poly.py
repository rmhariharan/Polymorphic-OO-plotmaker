import pandas as pd
import seaborn as sns

class DataReader():
    '''Opens and reads in as dataframe the input data files. Specify an input file (.csv),
       an output file (.png).First column should be entity names (e.g. gene names),
       and first row should be sample names'''
    
    def __init__(self,mydata,output_file):
        self.mydata = mydata
        self.output_file = output_file

        # Read data in
        self.df = pd.read_csv(self.mydata, header = 0,index_col = 0,mangle_dupe_cols = False)
        
        
class HeatMapMaker(DataReader):
        
    def plotmaker(self):
        '''A function for making heatmap with sample names on x-axis, entity names on y-axis.
           Assumes a dataframe with row and column names'''
    
        sns.set(font_scale = 0.65)


        mydf = self.df.drop(self.df.index,axis = 1)
        mydf = mydf.drop(mydf.index[0],axis = 0)
                
        entity_names = (self.df.index).tolist()
        sample_ids = (self.df.columns).tolist()
        
        g = sns.heatmap(mydf,xticklabels = sample_ids,yticklabels = entity_names,label = 'small',robust = False,cmap = "YlOrBr",cbar = True)
        sns.plt.xticks(rotation = 0)

        ##from matplotlib.patches import Rectangle
        ##ax1 = g.add_patch(Rectangle((0, 59), 37, 0, fill=False, edgecolor='orange', lw=0.6))

        ## Save figure to local disk
        
        sns.plt.savefig(self.output_file,format = 'png',bbox_inches = 'tight',dpi = 300)
        sns.plt.close()
        
        ##sns.plt.show()
        return "Completed"
    
class BarPlotMaker(DataReader):
    
    def plotmaker(self):
        '''Function to make bar plots. Input is a csv file. And output file needs to be specified'''

        sns.set(font_scale = 0.75)
        sns.set_style("whitegrid", {"axes.linewidth": "0","axes.labelcolor":"0.8"})
        sns.despine()

        sns.plt.figure(figsize = (8,1.1), dpi = 300)
        sns.barplot(data = self.df, palette = "Blues")

        ## Save figure to local drive
        
        sns.plt.savefig(self.output_file,format = 'png',dpi = 300,bbox_inches = 'tight')
        sns.plt.close()
        assert self.output_file.endswith(".png")
        return "Completed"

        #mybar.set(ylabel = "Number of pathways")
        #sns.plt.show()

