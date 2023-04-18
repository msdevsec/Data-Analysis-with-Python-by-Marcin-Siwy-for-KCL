import pandas as pd

# Load the dataset
df = pd.read_csv('data.csv')

#add naming to strenght values
df['strength'] = df['strength'].replace(['weak', 'medium', 'strong'], [0, 1, 2])

#calculate the mean 
mean_strength = df['strength'].mean()

#print results
print("The mean password strength is:", mean_strength)