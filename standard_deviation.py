import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv('data.csv')

# Calculate the standard deviation of the strength column
std_dev = df['strength'].std()

# Plot a graph toisualise results
plt.hist(df['strength'], bins=3, alpha=0.5)
plt.axvline(df['strength'].mean(), color='blue', linestyle='dashed', linewidth=1)
plt.axvline(df['strength'].mean()+std_dev, color='red', linestyle='dashed', linewidth=1)
plt.axvline(df['strength'].mean()-std_dev, color='red', linestyle='dashed', linewidth=1)
plt.xlabel('Strength')
plt.ylabel('Frequency')
plt.title('Distribution of Password Strengths')
plt.text(df['strength'].mean()-0.3, 200, "Standard Deviation: {}".format(round(std_dev,2)), fontsize=12, color='red')
plt.show()
