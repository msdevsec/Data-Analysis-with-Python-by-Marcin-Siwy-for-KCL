import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('data.csv', nrows=10000)

# Encode the password column as numeric values
df['password'] = df['password'].apply(lambda x: len(str(x)))
df = df.rename(columns={'password': 'length'})

# Create a scatter plot to visualize the relationship between password length and strength
sns.scatterplot(x='length', y='strength', data=df)
plt.xlabel('Password Length')
plt.ylabel('Password Strength')
plt.title('Password Strength by Password Length')
plt.show()
