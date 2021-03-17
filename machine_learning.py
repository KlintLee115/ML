import numpy as np
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier

vectorize = TfidfVectorizer(stop_words='english')

with open('words.txt') as fil:
    content=fil.readlines()
documents = [x.strip() for x in content] 

# print(documents)
x = vectorize.fit_transform(documents)
Y1 = vectorize.transform(["Can you help me with something?"])
prediction = kmeans.predict(Y1)
Y2 = vectorize.transform(["Just kidding tho"])
prediction2 = kmeans.predict(Y2)

# print(order_centroids)
# print(labels)
print(prediction)
print(prediction2)

# 0 = command
# 1 = statement