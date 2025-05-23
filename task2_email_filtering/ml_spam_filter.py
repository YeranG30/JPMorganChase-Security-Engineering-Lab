# import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# load the email dataset
df = pd.read_csv('emails.csv')

# show basic data structure
print(df.head())

# prepare features and labels
x = df['text']  # email body
y = df['label']  # spam = 1, ham = 0

# split the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# convert text into tf-idf feature vectors
vectorizer = TfidfVectorizer(stop_words='english')
x_train_vec = vectorizer.fit_transform(x_train)
x_test_vec = vectorizer.transform(x_test)

# train a naive bayes classifier
clf = MultinomialNB()
clf.fit(x_train_vec, y_train)

# make predictions
y_pred = clf.predict(x_test_vec)

# evaluate the model
print("accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
