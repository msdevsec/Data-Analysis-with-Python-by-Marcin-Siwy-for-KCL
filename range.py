import pandas as pd

# load the dataset
df = pd.read_csv('data.csv')

# Find the maximum and minimum values of 'strength' column
max_strength = df['strength'].max()
min_strength = df['strength'].min()

# Calculate the range
range_strength = max_strength - min_strength

# Print the results
print("The range of password strength is:", range_strength)

