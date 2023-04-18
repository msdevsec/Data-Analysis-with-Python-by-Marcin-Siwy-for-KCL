import pandas as pd
import matplotlib.pyplot as plt

# load the dataset
df = pd.read_csv("data.csv")

# calculate frequency of  strength
strength_freq = df['strength'].value_counts()

# sort results in descending order
strength_freq = strength_freq.sort_values(ascending=False)

# calculate the cumulative percentage
cumulative_perc = 100 * strength_freq.cumsum() / strength_freq.sum()

# plot Pareto chart
fig, ax1 = plt.subplots()

ax1.bar(strength_freq.index, strength_freq, color='tab:blue')
ax1.set_xlabel('Password Strength')
ax1.set_ylabel('Frequency', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.plot(strength_freq.index, cumulative_perc, color='tab:red', marker='o')
ax2.set_ylabel('Cumulative Percentage', color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')
ax2.set_ylim([0,100])

plt.title('Pareto Chart of password strength Frequency')
plt.show()
