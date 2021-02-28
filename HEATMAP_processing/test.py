import pandas as pd
import geopandas as gpd
import pdb
import matplotlib.pyplot as plt




def sentimentAnalysis(data):
	return data

def test():
	data = pd.read_csv('filte_data.csv')
	data = data.groupby('country').sum()
	pdb.set_trace()
	world = gpd.read_file(r'country.shp')

	world.replace('Brazil','Brasil',inplace = True)
	world.replace('Italy','Italia',inplace = True)


	merge = world.join(data,on ='name', how = 'right' )
	ax = merge.plot(column='agreg',
	                cmap = 'OrRd',
	                figsize=(10,5),
	                legend=True,
	                edgecolor = 'black',
	                linewidth =0.4
	                )
	plt.show()


if __name__=="__main__":
	test()