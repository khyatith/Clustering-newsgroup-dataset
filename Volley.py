from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics

categories = None

newsgroups_train = fetch_20newsgroups(subset='train')
labels = newsgroups_train.target

true_k = 12

#vectorize

vectorizer = TfidfVectorizer(max_df=0.5,
                             min_df=2,
                             stop_words='english')


X = vectorizer.fit_transform(newsgroups_train.data)

#clustering
km = KMeans(n_clusters=20, init='k-means++', max_iter=100, n_init=1)

km.fit(X)

order_centroids = km.cluster_centers_.argsort()[:, ::-1]

terms = vectorizer.get_feature_names()

for i in range(true_k):
    print("cluster %d:" % i)
    for ind in order_centroids[i,:20]:
        print('%s' % terms[ind])
    print()

#Performance
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels, km.labels_))
print("Completeness: %0.3f" % metrics.completeness_score(labels, km.labels_))
print("V-measure: %0.3f" % metrics.v_measure_score(labels, km.labels_))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, km.labels_, sample_size=1000))



