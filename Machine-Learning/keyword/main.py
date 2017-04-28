import numpy as np
import pandas as pd
import numpy.random as rd
import scipy.stats as st
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt

from matplotlib import gridspec
from matplotlib import animation as ani
plt.style.use('ggplot')
plt.rc('text', usetex=True)

import sys
import sklearn.metrics as mt

rd.seed(7)

# データから分布を生成
def get_density(data, xx, bw=.25):
    density = gaussian_kde(data)
    ensity.covariance_factor = lambda : bw
    density._compute_covariance()
    return density(xx)

n_row = 2    # グラフの行数
n_col = 2    # グラフの列数

plt.subplots(n_row, n_col, figsize=(16,7)) 
gs = gridspec.GridSpec(n_row, n_col)

axs = [plt.subplot(gs[i]) for i in range(4) ]

# 1つ目のエリア描画
rd.seed(0)
n = 141            # データ数
x = np.linspace(0,140,n)
y = rd.exponential(1.5, n) * 300
col = ["#2F79B0" for _ in range(n)] 
for i in range(5):    
    y[60+i] = rd.exponential(1.5, 1) * 300 + 2000
    col[60+i] = "r"
axs[0].scatter(x,y, c=col)
axs[0].set_xlim(-5,145)
axs[0].set_xlabel('time',size=12)


# 2つ目のエリア描画
n=80
xx = np.linspace(0, 3*np.pi, n)
x = np.linspace(0,10,n)
y = np.sin(xx) + rd.normal(0, 0.05, n)
col = ["#2F79B0" for _ in range(n)] 
for i in range(2):    
    y[48+i] += + 0.7
    col[48+i] = "r"
axs[1].scatter(x,y, c=col)
axs[1].set_xlim(0,10)
axs[1].set_ylim(-1.1,1.1)
axs[1].set_xlabel('time',size=12)


# 3つ目のエリア描画
x = None
y = None
n = 90


for i in range(3):
    x = np.linspace((3*i)*np.pi,(3*(i+1))*np.pi,100)
    a = 4 if i != 1 else 8
    y = np.sin(a*x) + rd.normal(0, 0.05, 100)

    c = "#2F79B0" if i != 1 else "r" 
    axs[2].plot(x, y, c=c, alpha=0.7)

axs[2].set_xlim(0,30)
axs[2].set_ylim(-1.1, 1.1)

# 4つ目のエリア描画
# 心電図データは下記より取得してください。
# http://vivonoetics.com/support/data-files/
# [Compact CSV sample import file](http://vivonoetics.com/wp-content/downloads/download.php?file=Csv_Sample_File_Compact.csv)よりDL
#ecg = np.array(pd.read_csv("Csv_Sample_File_Compact.csv").ECG[1100:3000])
#ecg = ecg/100.
#x = np.linspace(214, 222, len(ecg))

#axs[3].plot(x[0:300], ecg[0:300], c="#2F79B0")

#x2 = np.linspace(-1,1,199)
#x2 = np.linspace(-1,1,199)
#y2 = .2*x2**2 +.8
#print(x[301:500].shape)

#axs[3].plot(x[301:500], ecg[301:500]*y2, c="r", alpha=.6)
#axs[3].plot(x[501:], ecg[501:], c="#2F79B0")

plt.subplots_adjust()
