#!/usr/bin/env python
# encoding: utf-8
'''
@author:ryk
'''
import numpy as np
import matplotlib.pyplot as plt

# x = [5, 10,20,40,60,80,99]
# # y=[0.863,0.869,0.868,0.872,0.874]#P
# # z=[0.796,0.801,0.804,0.809,0.809]#R
# h = [0.65, 0.65,0.78,0.83,0.845,0.845,0.897]#f1
# t=[0.62,0.64,0.74,0.81,0.84,0.847,0.88]

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x=[40,80,120,160]
# h=[0.8365,0.8476,0.8676,0.8621]
# t=[0.7971,0.8269,0.8453,0.8629]

# h=[0.8283,0.8571,0.8433,0.8854]
# t=[0.6088,0.7021,0.7384,0.8178]
# z=[0.6789,0.7188,0.7613,0.8331]
#
#
# h=[0.8481,0.8591,0.8626,0.8669]
# t=[0.8350,0.8505,0.8542,0.8669]
# z=[0.8324,0.8506,0.8475,0.8629]


h=[  0.8271,0.8549, 0.8603,0.8966]
t=[0.7425,0.7969, 0.8152,0.8573]
# z=[ 0.7425,0.7969,0.8152,0.8573]


# h=[0.6870,0.7424,0.7882,0.8417]
# t=[0.6727,0.7422,0.7982,0.8641]
# z=[0.8368,0.8560,0.8625,0.8995]






plt.figure()
plt.xlabel("Training data set",fontsize=15)
plt.ylabel("F measure",fontsize=15)
# plt.plot(x, y,label="P scroe")
# plt.plot(x, z,label="R scroe")


# plt.plot(x,z,label="New Bert Embedding")
plt.plot(x, t,label="Without Transfer Learning")
plt.plot(x,h,label='Transfer Learning')

# plt.plot(x,z,label="Transfer Learning")
# plt.plot(x, t,label="Without Transfer Learning")
# plt.plot(x,h,label='Without Embedding')

# for a,b in zip(x,h):
#     # plt.text(x, y+0.3, '%.0f'%y, ha='center', va='bottom', fontsize=10.5)
#     plt.text(a, b + 0.0004, str(b), ha='center', va='bottom', fontsize=12)
#
#
# for a,b in zip(x,t):
#     # plt.text(x, y+0.3, '%.0f'%y, ha='center', va='bottom', fontsize=10.5)
#     plt.text(a, b - 0.002, str(b), ha='center', va='bottom', fontsize=12)

# plt.title('癌症文本迁移慢阻肺结果对比图')
plt.legend(loc=4,ncol=2)
plt.show()
plt.savefig("easyplot.jpg")
