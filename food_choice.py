import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np
from matplotlib import style


t = pd.read_csv("dataset.csv")
df = pd.DataFrame(t)

def category(attribute):
	# attributes=['Beauty','Food','Electronics','Entertainment','Medical','Schools','Shopping']
	if attribute == 1:
		beauty()
	elif attribute == 2:
		food()
	elif attribute == 3:
		electronics()
	elif attribute == 4:
		entertainment()
	elif attribute == 5:
		medical()
	elif attribute == 6:
		schools()
	elif attribute == 7:
		shopping()
def cate(name,aven,score,lst):
	print '\n\tAvenues with Respect to '+ name +' Category \n'
	b=df['Avenues'][df[name]].unique()
	print b
	
	print '\n\tBest Avenue for '+ name +' Category \n' 
	tbmax = df['Avenues'][df[name]].max()
	print tbmax
	
	print '\n\tLeast five for '+ name +' \n'
	tbmin = df['Avenues'][df[name]].min()
	print tbmin

	#list that describes what is under Shopping Category
	print '\n\tList of services under '+ name +' Category \n'
	bae = lst
	bae1 = pd.DataFrame(bae)
	print bae1[0]
def plot(name,aven,score):
	aven = aven
	xlen = np.arange(len(aven))
	yheight = score
	fig1, ax = plt.subplots(1,1)
	style.use('ggplot')
	plt.bar(xlen,yheight)
	plt.xlabel('Avenues')
	plt.ylabel('Scores')
	plt.xticks(xlen,aven)
	plt.title('Avenues with Respect to '+ name +'',{'fontsize':20})
	plt.tight_layout()
	plt.show()
def beauty():
	name = 'Beauty'
	aven = ['Anthem','Bel','Az','Avondale']
	score = [1,4,3,2]
	lst = ['Eyelash Service','Hair Removal','Beauty & Spas','Hair Salons', 'Day Spas', 'Skin Care', 'Barbers', 'Massage', 'Nail Salons']
	cate(name,aven,score,lst)
	plot(name,aven,score)
def food():
	name = 'Food'
	aven = ['Az','Bel','Avondale','Anthem','Bend']
	score = [3,4,2,1,5]
	lst = ['']
	cate(name,aven,score,lst)
	plot(name,aven,score)
def electronics():
	name = 'Electronis'
	aven = ['Anthem','Avondale','Az','Ahwatukee','Bel']
	score = [1,2,3,0,4]
	lst = ['Lighting Fixtures & Equipment','Appliances','Hardware Stores','Photographers','Musical Instruments & Teachers','Electronics']
	cate(name,aven,score,lst)
	plot(name,aven,score)
def entertainment():
	name = 'Entertainment'
	aven = ['Avondale','Anthem','Az','Bel','Ahwatukee']
	score = [2,1,3,4,0]
	lst = ['Resorts','Print Media','Modern European','Jazz & Blues','Videos & Video Game Rental','Russian','Museums','Gastropubs','Books, Mags, Music & Video','Tattoo','Mass Media','Musical Instruments & Teachers','Arts & Entertainment','Music & DVDs','Nightlife']
	cate(name,aven,score,lst)
	plot(name,aven,score)
def medical():
	name = 'Medical'
	aven = ['Anthem','Bel','Az','Bend','Avondale']
	score = [1,4,3,5,2]
	lst = ['Active Life','Medical Centers', 'Pediatric Dentists','Oral Surgeons','Reflexology','Neurologist','Weight Loss Centers','Acupuncture','Nutritionists','Dermatologists','Health Markets','Health & Medical','Health Markets','Veterinarians','Optometrists','Doctors','Allergists', 'Department Stores']
	cate(name,aven,score,lst)
	plot(name,aven,score)
def schools():
	name = 'Schools'
	aven = ['Anthem','Az']
	score = [1,3]
	lst = ['Art Schools','Cosmetology Schools']
	cate(name,aven,score,lst)
	plot(name,aven,score)
def shopping():
	name = 'Shopping'
	aven = ['Anthem','Bel','Az','Avondale']
	score = [1,4,3,4]
	lst = ['Fashion','Gift Shops','Bridal','Shopping', 'Flowers & Gifts', 'Sporting Goods', 'Leather Goods', 'Lingerie', "Women's Clothing","Men's Clothing" ,'Used, Vintage & Consignment', 'Shopping Centers']
	cate(name,aven,score,lst)
	plot(name,aven,score)
