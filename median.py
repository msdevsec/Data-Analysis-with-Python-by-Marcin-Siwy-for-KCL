import pandas as pd

# Read the dataset 
df = pd.read_csv('data.csv')

# Calculate the median of the strength column
median_strength = df['strength'].median()

# Print the result
print("The median password strength is:", median_strength)

