import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets

# データ良いm込み
diabetes = datasets.load_diabetes()

# データを訓練/評価で分ける
data_train   = diabetes.data[:-20]
target_train = diabetes.target[:-20]
data_test    = diabetes.data[-20:]
target_test  = diabetes.target[-20:]

# 学習
lin = linear_model.LinearRegression()
lin.fit(data_train, target_train)

# 当てはまり度合い
print("Score : ", lin.score(data_test, target_test))

print("Prediction :", lin.predict(data_test[0]))
print("Actual Value :", target_test[0])
