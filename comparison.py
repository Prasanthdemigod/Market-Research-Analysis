# comparison
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

t = pd.read_csv("dataset.csv")
df = pd.DataFrame(t)

def comp():
	print df['Avenues']
	choice1 = raw_input("\nSelect an Avenue for comparison\n")
	choice2 = raw_input("\nSelect another Avenue for comparison\n")
	if(choice1==choice2):
	plot(choice1,choice2)

def plot(choice1,choice2):

	val1=[]
	val2=[]

	b1=df[['Beauty','Food','Electronics','Entertainment','Medical','Schools','Shopping']][df['Avenues']==choice1]
	val1=b1.iloc[0,]

	b2=df[['Beauty','Food','Electronics','Entertainment','Medical','Schools','Shopping']][df['Avenues']==choice2]
	val2=b2.iloc[0,]

	X= np.arange(7)
	label1=['Beauty','Food','Electronics','Entertainment','Medical','Schools','Shopping']
	style.use('ggplot')
	
	plt.bar(X + 0.00, val1, color = 'b', label= choice1 ,width = 0.25)
	plt.bar(X + 0.25, val2, color = 'g', label= choice2 ,width = 0.25)
	plt.ylabel("Scores")
	plt.xlabel("Category")
	locs, labels = plt.xticks(X,label1)
	plt.setp(labels, rotation=15)
	plt.title('Comparison chart for '+choice1+' & '+choice2 ,{'fontsize':20})
	plt.legend()
	plt.tight_layout
	plt.show()

if __name__ == '__main__':
	comp()
