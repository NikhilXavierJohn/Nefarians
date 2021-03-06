import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as numpy
import re
import string
import warnings
import random
warnings.simplefilter('ignore',DeprecationWarning)
dataset = pd.read_csv("thanks.csv")
def clean_text(s):
    s = s.lower()
    for ch in string.punctuation:                                                                                                     
        s = s.replace(ch, " ") 
    s = re.sub("[0-9]+", "||DIG||",s)
    s = re.sub(' +',' ', s)        
    return s

dataset['TEXT'] = [clean_text(s) for s in dataset['TITLE']]


# pull the data into vectors
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(dataset['TEXT'])

# for Tfidf (we have tried and the results aren't better)
#tfidf = TfidfVectorizer()
#x = tfidf.fit_transform(dataset['TEXT'].values)

encoder = LabelEncoder()
y = encoder.fit_transform(dataset['CATEGORY'])

# split into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# take a look at the shape of each of these
# print(x_train.shape)
# print(y_train.shape)
# print(x_test.shape)
# print(y_test.shape)

nb = MultinomialNB()
nb.fit(x_train, y_train)
results_nb_cv = cross_val_score(nb, x_train, y_train, cv=10)
#print(results_nb_cv.mean())
nb.score(x_test, y_test)
x_test_pred = nb.predict(x_test)
confusion_matrix(y_test, x_test_pred)
#print(classification_report(y_test, x_test_pred, target_names=encoder.classes_))
results_nb_cv = cross_val_score(nb, x_train, y_train, cv=10)
# print(str(results_nb_cv.mean()*100)+"%")
def predict_cat(title):
    cat_names = {'b' : 'business', 't' : 'science and technology', 'et' : 'entertainment', 'm' : 'health', 'w' : 'weather', 'ed' : 'education', 'c' : 'crime', 'sp' : 'sports'}
    cod = nb.predict(vectorizer.transform([title]))
    return cat_names[encoder.inverse_transform(cod)[0]]
def fetchandget(summary):
    category=predict_cat(summary)
    print(category)
    import csv
    if(category=="business"):
            category="b"
    elif(category=="science and technology"):
        category="t"
    elif(category=="entertainment"):
        category="et"
    elif(category=="health"):
        category="m"
    elif(category=="weather"):
        category="w"
    elif(category=="education"):
        category="ed"
    elif(category=="crime"):
        category="c"
    elif(category=="sports"):
        category="sp"
    fields=[random.randint(1,5000),summary,category]
    with open('thanks.csv', 'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
fetchandget("rape is a crime")
