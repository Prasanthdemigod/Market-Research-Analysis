import pandas as pd
import json
import csv
import ast
from pandas import DataFrame


def Data_clean():

    '''
    First part of the cleaning process. Here all the missing data are corrected and replaced with appropriate values based on the data.
    Further splitting and avenue based processing is done.
    '''


    # Line 16 to 20 are used in the cleaning process when run for the first time alone

    # with open("/home/sois/Downloads/result(1).csv", "rb") as source:
    # 	rdr = csv.reader(source)
    # 	with open("/home/sois/Desktop/result.csv", "wb") as result:
    # 		wtr = csv.writer(result)
    # 		for r in rdr:
    # 			del r[75:]
    # 			del r[2:59]
    # 			wtr.writerow(r)
    Fdata = pd.read_csv("/home/prashanth/yelp/result(1).csv", index_col = False)
    df = DataFrame(Fdata)

    # Filtering rows with reviews >= 5 and putting it into another dataframe
    df_1 = df[df['reviews/total'] >= 5]
    print("length of df_1",len(df_1))
    dd = DataFrame(df_1)
    dd.to_csv("new_results.csv")

    with open("/home/prashanth/yelp/new_results.csv", "rb") as source:
        results_data = csv.reader(source)
        for r in results_data:
            print r

    new_Data = pd.read_csv("/home/prashanth/yelp/new_results.csv")
    df_2 = DataFrame(new_Data)

    #Splitting data into tokens based on space delimiter and addressing the avenues alone
    for index in df_2.index:
        if df_2['location/address'][index] is not None:
            text = df_2['location/address'][index]
            splitted = text.split()
            if len(splitted) <= 3:
                df_2['location/address'][index] = "4131 N 24th St Ste 217 Phoenix, AZ 85016"

    location = df_2['location/address']

    #just testing
    #for loc in location:
    # text = df_2.loc[2392]
    # dest = text['location/address']
    # AR = dest.split()
    # avenue = AR[-3]
    # avenue = avenue[:-1]
    # print avenue


    # Getting the Geo-Avenues alone from the addresses

    lst = []
    import re
    count = 0
    for loc in location:
        count += 1
        text = loc.split()
        avenue = text[-3]
        avenue = avenue[:-1]
        lst.append(avenue)


    #Adding a new column Avenues with only avenues instead of the whole address
    df_2['Avenues'] = pd.Series(lst, index = df_2.index)
    df_2.to_csv("/home/prashanth/yelp/new.csv", sep = '\t')


    # Cleaning the data for Columns like Reviews, Stars, Avenues, All categories
    Stars = df_2['stars']
    import math
    for ind in df_2.index:
        if math.isnan(df_2['stars'][ind]):
            df_2['stars'][ind] = 3.5

    return df_2


def Grouping_data(df_2):

    # Cleaning data by grouping similar categories under one roof

    unique_categories = df_2[:]['categories/0'].unique()
    avenues = df_2[:]['Avenues']

    print unique_categories

    Shopping = ['Fashion','Gift Shops','Bridal','Shopping', 'Flowers & Gifts', 'Sporting Goods', 'Leather Goods', 'Lingerie', "Women's Clothing","Men's Clothing" ,'Used, Vintage & Consignment', 'Shopping Centers']
    Beauty = ['Eyelash Service','Hair Removal','Beauty & Spas','Hair Salons', 'Day Spas', 'Skin Care', 'Barbers', 'Massage', 'Nail Salons']
    Medical = ['Active Life','Medical Centers', 'Pediatric Dentists','Oral Surgeons','Reflexology','Neurologist','Weight Loss Centers','Acupuncture','Nutritionists','Dermatologists','Health Markets','Health & Medical','Health Markets','Veterinarians','Optometrists','Doctors','Allergists', 'Department Stores']
    Electronics = ['Lighting Fixtures & Equipment','Appliances','Hardware Stores','Photographers','Musical Instruments & Teachers','Electronics']
    Entertainment = ['Resorts','Print Media','Modern European','Jazz & Blues','Videos & Video Game Rental','Russian','Museums','Gastropubs','Books, Mags, Music & Video','Tattoo','Mass Media','Musical Instruments & Teachers','Arts & Entertainment','Music & DVDs','Nightlife']
    Schools = ['Art Schools','Cosmetology Schools']

    for ind in df_2.index:
        if df_2['categories/0'][ind] in Shopping:
            df_2['categories/0'][ind] = "Shopping"
        elif df_2['categories/0'][ind] in Beauty:
            df_2['categories/0'][ind] = "Beauty"
        elif df_2['categories/0'][ind] in Medical:
            df_2['categories/0'][ind] = "Medical"
        elif df_2['categories/0'][ind] in Electronics:
            df_2['categories/0'][ind] = "Electronics"
        elif df_2['categories/0'][ind] in Entertainment:
            df_2['categories/0'][ind] = "Entertainment"
        elif df_2['categories/0'][ind] in Schools:
            df_2['categories/0'][ind] = "Schools"
        else:
            df_2['categories/0'][ind] = "Food"

    ddd = {'Avenues': df_2['Avenues'], 'Categories': df_2['categories/0'], 'Reviews': df_2['reviews/total'], 'Stars':df_2['stars'] }
    df_3 = DataFrame(data = ddd)

    # Grouping data as per Geos
    grouped_1 = df_3.groupby('Avenues')
    for Geo, group in grouped_1:
        print Geo
        print group

    return df_3


def Normalize_scores(df_3):

    '''Allocating scores as per the number of reviews. This is used to bring about all the categories under one roof
       through Normalization so that we can make comparisons and draw decisions'''

    max_value = max(df_3['Reviews'])
    print "The maximum review is ", max_value
    no_of_scores = (max_value/10)
    d = [None]*no_of_scores
    for i in range(no_of_scores):
        d[i] = i
    Re = [None]*len(df_3)
    start = 5
    for ind in df_3.index:
        review_count = df_3['Reviews'][ind]
        index = review_count/10
        Re[ind] = (review_count - (index * 10))*df_3['Stars'][ind]*d[i]

    df_3['Scores'] = pd.Series(Re, index = df_3.index)
    print "Printing df_3"
    print df_3

    import numpy as np

    mean = np.mean(df_3['Scores'])
    print "Mean is", mean

    # Calculating Variance and Standard Deviation for the Scores

    Review_length =len(df_3['Reviews'])
    VA = 0
    for i in range(Review_length):
        VA += (df_3['Scores'][i] - mean)**2
    SDD = VA/(Review_length-1)
    SD = np.sqrt(SDD)
    print "The Standard Deviation is :", SD

    # Now for each Score value, we will be finding the normalized value
    for i in range(Review_length):
        df_3['Scores'][i] = (df_3['Scores'][i] - mean)/SD
    print "df_3 is ",df_3
    df_3.to_csv('newdf_3.csv')

    Latest_data = pd.read_csv('/home/prashanth/yelp/new_one.csv')

    return df_3


def Data_preprocess(df_3):
    '''
    Here the data is preprocessed and fed to Machine Learning Algorithms
    '''


    from sklearn import preprocessing
    import numpy as np

    Score_train = np.array(df_3['Scores'])
    Score_scaled = preprocessing.scale(Score_train)
    print "Scaled Score: ",Score_scaled

    # Now assigning numerical values to Avenues column so as to ease in Data preprocessing

    unique_avenues = df_3['Avenues'].unique()
    unique_categories = df_3['Categories'].unique()
    print 'unique avenues', unique_avenues
    print 'Unique Categories', unique_categories

    count = 0

    # Alloting unique numbers to unique categories

    for av in unique_avenues:
        for ind in df_3.index:
            if df_3['Avenues'][ind] == av:
                df_3['Avenues'][ind] = count

        count += 1

    count = 120

    for cat in unique_categories:
        for ind in df_3.index:
            if df_3['Categories'][ind] == cat:
                df_3['Categories'][ind] = count
        count -= 1

    print df_3

    df_3.set_index(['Avenues', 'Categories'])
    print df_3.groupby(['Avenues', 'Categories'])['Scores'].sum()
    new_data = df_3.groupby(['Avenues', 'Categories'])['Scores'].sum()

    df_3.to_csv("new_geo.csv")

    from sklearn import datasets

    Category_Avenues_normalized = preprocessing.normalize(df_3[['Avenues', 'Categories', 'Scores']])
    Category_Avenues_scores = np.array(df_3[['Avenues', 'Categories', 'Scores']])
    Category_Avenues_scores_scaled = preprocessing.scale(Category_Avenues_scores)

    print "printing Normalized Category values :", Category_Avenues_normalized
    print "Scaled Avenue values: ", Category_Avenues_scores_scaled

    df_4 = DataFrame(data = Category_Avenues_normalized)
    df_4.columns = {'Avenues','Category', 'Scores' }

    print df_4
    df_4.to_csv("preprocessed_data.csv")

    df_5 = DataFrame(data = Category_Avenues_scores_scaled)
    df_5.columns = {'Avenues', 'Categories', 'Scores'}

    print df_5
