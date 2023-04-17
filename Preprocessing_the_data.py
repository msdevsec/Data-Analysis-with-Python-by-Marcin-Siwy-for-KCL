python

import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv('data.csv')

# Save a copy of the default frame
original_df = df.copy()

# Remove duplicate entries
df.drop_duplicates(inplace=True)
duplicates_removed = len(original_df) - len(df)

#remove empty rows
df.dropna(inplace=True)
empty_rows_removed = len(original_df) - len(df) - duplicates_removed

# Calculate total rows that were  deleted
total_rows_removed = duplicates_removed + empty_rows_removed

# Create a graph to show the number of rows removed at each step and display total rows removed
labels = ['Duplicates', 'Empty Rows']
removed_rows = [duplicates_removed, empty_rows_removed]

plt.bar(labels, removed_rows)
plt.title(f'Rows Removed During Cleaning Process\nTotal Rows Deleted: {total_rows_removed}')
plt.ylabel('Number of Rows Removed')
plt.show()