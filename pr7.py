import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.mixture import GaussianMixture
import sklearn.metrics as sm
import pandas as pd
import numpy as np
iris = pd.read_csv('/home/mllab03/PycharmProjects/AIML/datasets/iris_data.csv')
iris['Targets'] = iris.Class.map({'iris-setosa':0, 'iris-versicolor':1, 'iris-virginica':2})
X = iris[['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width' ] ]
Y = iris[['Targets']]
model = KMeans(n_clusters = 3)
model.fit(X)
print('Model Labels:\n', model.labels_ )
scaler = preprocessing.StandardScaler()
scaler.fit(X)
xs = scaler.transform(X)
gmm = GaussianMixture(n_components = 3)
gmm.fit(xs)
Y_gmm = gmm.predict(xs)
print('GMM Labels:\n', Y_gmm)
plt.figure(figsize = (10, 10))
colormap = np.array(['red', 'lime', 'black'])
plt.subplot(2, 2, 1)
plt.scatter(X.Petal_Length,X.Petal_Width, c = colormap[Y.Targets], s=40)
plt.title('Real Classification')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.subplot(2, 2, 2)
plt.scatter(X.Petal_Length,X.Petal_Width, c = colormap[model.labels_], s=40)
plt.title('K Means Clustering')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.subplot(2, 2, 3)
plt.scatter(X.Petal_Length, X.Petal_Width, c = colormap[Y_gmm], s=40)
plt.title('GMM Based Clustering')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
print('Evaluation of K-Means with ground truth classification of Iris Dataset')
print('Rand Index:%f ' % sm.adjusted_rand_score(Y.Targets, model.labels_ ))
print('Homogenity Score:%f ' % sm.homogeneity_score(Y.Targets, model.labels_ ))
print('Completeness Score:%f ' % sm.completeness_score(Y.Targets, model.labels_ ))
print('V-Measure:%f ' % sm.v_measure_score(Y.Targets, model.labels_ ))
print('Evaluation of GMM with ground truth classification of Iris Dataset')
print('Rand Index:%f ' % sm.adjusted_rand_score(Y.Targets, Y_gmm))
print('Homogenity Score:%f ' % sm.homogeneity_score(Y.Targets, Y_gmm))
print('Completeness Score:%f ' % sm.completeness_score(Y.Targets, Y_gmm))
print('V-Measure:%f ' % sm.v_measure_score(Y.Targets, Y_gmm))


