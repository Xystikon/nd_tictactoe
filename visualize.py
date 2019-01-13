import numpy as np
import tkinter as tk
import copy
import pickle as pickle    # cPickle is available in Python 2.x only, otherwise use pickle
import matplotlib
import matplotlib.pyplot as plt

#from q_learning import Game, HumanPlayer, QPlayer

Q = pickle.load(open("p_files/Q_epsilon_0.9_Nepisodes_1000_N_5_alpha_0.3_gamma_0.2.p", "rb"))

x = np.zeros(len(Q)+1)
y = np.zeros(len(Q)+1)
y2 = np.zeros(len(Q)+1)

i=0
for outer_key, inner_dict in Q.items():
    sum_values_X = 0.0
    sum_values_O = 0.0
    i = i+1
    if outer_key.endswith("X"):
        #sort_them = sorted(outer_key)
        print("outer_key", outer_key)
        for inner_key, value in inner_dict.items():
        #     print("outer=", outer_key)
        #     print("inner=", inner_key)
        #     print("value=", value)
             sum_values_X= sum_values_X + value
    if outer_key.endswith("O"):
        #sort_them = sorted(outer_key)
        print("outer_key", outer_key)
        for inner_key, value in inner_dict.items():
        #     print("outer=", outer_key)
        #     print("inner=", inner_key)
        #     print("value=", value)
             sum_values_O= sum_values_O + value
    y[i] = sum_values_X
    y2[i] = sum_values_O
    x[i] = i
    print("sum_values_X",y[i])
    print("sum_values_O",y2[i])
    print("i", x[i])


plt.plot(x,y)
axes = plt.gca()
axes.set_ylim([0,np.max(y)])
axes.set_xlim([0,len(Q)])

plt.savefig('output/QX.png')
plt.close()

plt.plot(x,y2)
axes = plt.gca()
axes.set_ylim([0,np.max(y2)])
axes.set_xlim([0,len(Q)])

plt.savefig('output/QO.png')
