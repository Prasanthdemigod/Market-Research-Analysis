# overall 
import sys
import numpy as np
import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt

def overall():
	t = pd.read_csv("~/Desktop/dataset.csv")
	df = pd.DataFrame(t)

	beautysum = df['Beauty'].sum()
	foodsum = df['Food'].sum()
	electronicssum = df['Electronics'].sum()
	entertainmentsum = df['Entertainment'].sum()
	medicalsum = df['Medical'].sum()
	schoolssum = df['Schools'].sum()
	shoppingsum = df['Shopping'].sum()

	#plotPieChart()
	dfvalues = [beautysum,foodsum,electronicssum,entertainmentsum,medicalsum,schoolssum,shoppingsum]
	style.use("ggplot")
	labels= ['Beauty','Food','Electronics','Entertainment','Medical','Schools','Shopping']
	sizes = dfvalues
	explode = (0.03,0.02,0.03,0.03,0.03,0.03,0.03) 
	plt.pie(sizes, explode=explode, labels=labels, counterclock=True, autopct='%2.1f%%', shadow = False, startangle = 195)
	plt.axis=('equal')
	plt.title('Market Analysis for avenues in Arizona State',{'fontsize':18}) 
	plt.show()