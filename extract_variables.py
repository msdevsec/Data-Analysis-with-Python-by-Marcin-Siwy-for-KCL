import pandas as pd
#read the CSV file with the dataset
data = pd.read.csv('data.csv')

#Print only the first 10k rowns for this research purpose
print(data.head(10000)
     
#check the data types of the colomns
print(data.dtypes)
