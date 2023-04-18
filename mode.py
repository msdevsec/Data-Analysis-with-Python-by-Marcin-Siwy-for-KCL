import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv('data.csv')

# Calculate the mode of the strength column
mode_strength = df['strength'].mode()

# Count the frequency of each password strength value
password_strengths = df['strength'].value_counts()

# Graph the distribution of password strengths
plt.bar(password_strengths.index, password_strengths.values)
plt.title('Distribution of Password strength')
plt.xlabel('Strength')
plt.ylabel('Count')
plt.axvline(mode_strength[0], color='r', linestyle='dashed', linewidth=1)
plt.text(mode_strength[0], max(password_strengths.values)*0.8, 'Mode: {}'.format(mode_strength[0]))
plt.show()
