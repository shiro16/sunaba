import sklearn.datasets as datasets
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation

# データ読み込み
iris = datasets.load_iris()

# 2 のデータを削除
data = iris.data[iris.target != 2]
target = iris.target[iris.target != 2]

# 学習と交差検定による評価
logi = LogisticRegression()
scores = cross_validation.cross_val_score(logi, data, target, cv=5)

print(scores)
