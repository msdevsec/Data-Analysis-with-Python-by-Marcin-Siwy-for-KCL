import pandas as pd
import seaborn as sns

# load the dataset
df = pd.read_csv('data.csv')

# use only first 10k records
df = df.iloc[:10000]

# Encode the password column
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
df['password'] = encoder.fit_transform(df['password'])

# Calculate correlation matrix
corr_matrix = df.corr()

# Visualize results using a heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
