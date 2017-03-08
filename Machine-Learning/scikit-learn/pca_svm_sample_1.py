from sklearn import datasets
from sklearn import svm
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

iris = datasets.load_iris()

pca = PCA(n_components=2)
data = pca.fit(iris.data).transform(iris.data)

datamax = data.max(axis=0) + 1
datamin = data.min(axis=0) - 1
n = 200
X, Y = np.meshgrid(np.linspace(datamin[0], datamax[0], n), np.linspace(datamin[1], datamax[1], n))

svc = svm.SVC()
svc.fit(data, iris.target)
Z = svc.predict(np.c_[X.ravel(), Y.ravel()])

plt.contour(X, Y, Z.reshape(X.shape), colors="k")
for c, s in zip([0, 1, 2], ["o", "+", "x"]):
    d = data[iris.target == c]
    plt.scatter(d[:, 0], d[:, 1], c="k", marker=s)
plt.show()
