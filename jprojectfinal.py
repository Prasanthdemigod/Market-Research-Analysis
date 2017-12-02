import sys
import overall
import comparison
import food_choice
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

dfvalues = 0

def printAvenueChoice():
	print "\n\n"
	t = pd.read_csv("dataset_1.csv")
	df = pd.DataFrame(t)
	print df['Avenues'].unique()
	choice=raw_input("Enter the Avenue Name: \n")
	print("\nYou have selected "+choice)
	b=df['categories'][df['avenues']==choice]
	dfvalues = b.values

	#plotPieChart()
	style.use("ggplot")
	labels= ['Beauty','Electronics','Entertainment','Food','Medical','Schools','Shopping']
	plt.style.use('ggplot')
	sizes = dfvalues
	explode = (0.03,0.02,0.03,0.03,0.03,0.03,0.03) 
	plt.pie(sizes, explode=explode, labels=labels, counterclock=True, autopct='%2.1f%%', shadow = False, startangle = 195)
	plt.axis=('equal')
	plt.title('Market Analysis for '+choice,{'fontsize':18}) 
	plt.show()

def categorybased():
	print "\nAvailable Categories:\n\t1.Beauty\n\t\n\t2.Electronics\n\t3.Entertainment\n\t4.Food\n\t 5.Medical\n\t6.Schools\n\t7.Shopping\n"
	attributes=['Beauty','Electronics','Entertainment','Food','Medical','Schools','Shopping']
	while True:
		try:
			print "Choose Option :"
			value=int(input())
		except:
			print "Wrong choice!"
			continue
		if 1<=value<=7:
			food_choice.category(value)
			return
		print "Wrong choice!"
def main():
	
	print "\tMarket Analysis\n"
	Fdata = pd.read_csv("result(1).csv", index_col = False)
	print "Raw Dataset"
	original = pd.DataFrame(Fdata)
	print(original)
	print "Data Cleaning..."

	print "\n\tCleaned Dataset \n"
	t = pd.read_csv("~/Desktopdataset.csv")
	df = pd.DataFrame(t)
	print df 
	
	print "\nAnalysis and Visualization..."
	print "How do you like to Visualize? \n"
	
	while True:
		print "\t1.Avenue Based Visualization\n\t2.Category Based Visualization\n\t3.Overall Visualization\n\t4.Comparison Visualization\n\nEnter e/E to exit\nChoose option:",
		value=raw_input()
		try:
			value=int(value)
		except:
			if value.strip().lower()=='e':
				print "\n\t Thank You :) \n\n"
				return
		if value==1:
			printAvenueChoice() 
		elif value==2:
			categorybased()      
		elif value==3:
			overall.overall()
		elif value==4:
			comparison.comp()           
		print "\nAny other visualization?"
		
if __name__=="__main__":
	main()
