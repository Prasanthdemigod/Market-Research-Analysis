'''
A central
'''
import YelpCsv_parse as yp

df_2 = yp.Data_clean()
df_3 = yp.Grouping_data(df_2)
df_3 = yp.Normalize_scores(df_3)
yp.Data_preprocess(df_3)
