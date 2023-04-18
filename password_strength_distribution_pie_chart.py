import pandas as pd
import matplotlib.pyplot as plt

# load the dataset
df = pd.read_csv("data.csv")

# create frequency distribution
freq = df['strength'].value_counts()

# plot pie chart
plt.pie(freq, labels=freq.index, autopct='%1.1f%%')
plt.title('Password Strength Frequency Distribution')
plt.show()
