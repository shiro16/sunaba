# -*- coding: utf-8 -*-
import numpy as np
import scipy as sc
from scipy import linalg
from scipy import spatial
import scipy.spatial.distance
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager
import pylab

ROW = 6
COLUMN = 10
csv = pd.read_csv('test.csv')


# row:行,column:列,ave:平均,vcm:分散共分散行列
row = []
column = []
ave = [0.0 for i in range(ROW)]
vcm = np.zeros((COLUMN, ROW, ROW))
diff = np.zeros((1, ROW))
mahal = np.zeros(COLUMN)
tmp = np.zeros(ROW)


trans_data = csv.dropna(axis=1)
#print(trans_data)

# rowにtrans_dataの要素をリストの形式で連結
for i in range(ROW):
    row.append(list(trans_data.ix[i]))
#print(row)

# 列を連結
for i in range(1, COLUMN+1):
    column.append(list(trans_data.ix[:, i]))
#print(column)

# 平均値の計算
for i in range(ROW):
    # スライスという技法
    ave[i] = np.average(row[i][1:len(row[i])])
#print(ave)


# Numpyのメソッドを使うので，array()でリストを変換した．
column = np.array([column])
ave = np.array(ave)

# 分散共分散行列を求める
# np.swapaxes()で軸を変換することができる．
for i in range(COLUMN):
    diff = (column[0][i] - ave)
    diff = np.array([diff])
    vcm[i] = (diff * np.swapaxes(diff, 0, 1)) / COLUMN

# print(vcm)

# mahalnobis distanceを求める
for i in range(COLUMN):
    # 一般逆行列を生成し，計算の都合上転値をかける
    vcm[i] = sc.linalg.pinv(vcm[i])
    vcm[i] = vcm[i].transpose()
    vcm[i] = np.identity(ROW)
    # 差分ベクトルの生成
    diff = (column[0][i] - ave)
    for j in range(ROW):
        tmp[j] = np.dot(diff, vcm[i][j])
    mahal[i] = np.dot(tmp, diff)

print(mahal)


plot = pylab.arange(0.0, ROW, 1.0)
mahal = np.sqrt(mahal)

print("マハラノビス距離")
print(mahal)
plt.bar(range(COLUMN),mahal)
plt.title("")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("plot1.png")
