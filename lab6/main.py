# pip install sklearn
# pip install nltk
import time

import pandas as pd
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from models import OnlyInA, TF_IDF, Binary_weight
from models.vectorizing import vectorizing, vectorizing_voc

dataset_true = pd.read_csv('./data/True.csv', usecols=['title', 'text'])  # Read file
dataset_fake = pd.read_csv('./data/Fake.csv', usecols=['title', 'text'])
dataset_true["id"] = 1
dataset_fake["id"] = 0
concatenated = pd.concat([dataset_true, dataset_fake]).sample(20000)
together_dataset_vector, together_dataset_titles = vectorizing(concatenated['title'])


X_train, X_test, y_train, y_test = train_test_split(concatenated['title'], concatenated["id"],
                                                    test_size=0.33, random_state=42)

X_train_vector, X_train_titles = vectorizing_voc(X_train, together_dataset_titles)
X_test_vector, X_test_titles = vectorizing_voc(X_test, together_dataset_titles)

time1 = time.time()
DTC = DecisionTreeClassifier()
DTC.fit(X_train_vector, y_train)
y_pred = DTC.predict(X_test_vector)
print("Accuracy DTC:", metrics.accuracy_score(y_test, y_pred))
# print("Accuracy another way:", DTC.score(X_test_vector, y_test))
time2 = time.time()
print(f'Time of Classifying DTC: {(time2 - time1):.4f}')

RFC = RandomForestClassifier()
RFC.fit(X_train_vector, y_train)
y_pred = RFC.predict(X_test_vector)
print("Accuracy RFC:", metrics.accuracy_score(y_test, y_pred))
# print("Accuracy another way:", RFC.score(X_test_vector, y_test))
time3 = time.time()
print(f'Time of Classifying RFC: {(time3 - time2):.4f}')


svc = SVC()
svc.fit(X_train_vector, y_train)
# y_pred=SVC.predict(X_test_vector)
# print("Accuracy SVC:",metrics.accuracy_score(y_test, y_pred))
print("Accuracy SVC:", svc.score(X_test_vector, y_test))
time4 = time.time()
print(f'Time of Classifying SVC: {(time4 - time3):.4f}')


ABC = AdaBoostClassifier()
ABC.fit(X_train_vector, y_train)
y_pred = ABC.predict(X_test_vector)
print("Accuracy ABC:", metrics.accuracy_score(y_test, y_pred))
# print("Accuracy another way:", ABC.score(X_test_vector, y_test))
time5 = time.time()
print(f'Time of Classifying ABC: {(time5 - time4):.4f}')


BC = BaggingClassifier()
BC.fit(X_train_vector, y_train)
y_pred = BC.predict(X_test_vector)
print("Accuracy BC:", metrics.accuracy_score(y_test, y_pred))
# print("Accuracy another way:", BC.score(X_test_vector, y_test))
time6 = time.time()
print(f'Time of Classifying BC: {(time6 - time5):.4f}')

# OnlyInA.onlyInA(sample_true, sample_fake, "Top10 tokens only in True message", "top10_true")
# OnlyInA.onlyInA(sample_fake, sample_true, "Top10 tokens only in Fake message", "top10_fake")
# TF_IDF.TF_IDF(sample_fake, "Key tokens in Fake message based on TD-IDF", "TD-IDF_fake")
# Binary_weight.Binary_weight(sample_fake, "Crucial tokens in Fake message based on binary weight",
# "binary_weight_Fake")
