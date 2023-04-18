import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report

# load the dataset
df = pd.read_csv("data.csv", nrows=10000)


# split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['password'], df['strength'], test_size=0.2, random_state=42)

# vectorize the passwords
vectorizer = TfidfVectorizer(min_df=1, analyzer='char', ngram_range=(3, 3))
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# train the classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# make predictions on the test set
y_pred = classifier.predict(X_test)

# graph classification report and confusion matrix
print(classification_report(y_test, y_pred))
conf_mat = confusion_matrix(y_test, y_pred)
print(conf_mat)

# plot the confusion matrix in heatmap
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(conf_mat)
ax.xaxis.set(ticks=range(3))
ax.yaxis.set(ticks=range(3))
ax.set_xticklabels(['weak', 'medium', 'strong'], fontsize=12)
ax.set_yticklabels(['weak', 'medium', 'strong'], fontsize=12)
for i in range(3):
    for j in range(3):
        ax.text(j, i, conf_mat[i, j], ha='center', va='center', color='white')
plt.xlabel('Predicted label', fontsize=12)
plt.ylabel('True label', fontsize=12)
plt.show()

