import numpy as np
import tkinter as tk
import copy
import pickle as pickle    # cPickle is available in Python 2.x only, otherwise use pickle
import matplotlib
import matplotlib.pyplot as plt
import sklearn
from q_learning import Game, QPlayer  
from skopt import gp_minimize
from skopt.space import Real, Integer
import gc


def train_Q(a,g,epsilon,N,N_episodes):

    root = tk.Tk()
    player1 = QPlayer(mark="X",epsilon = epsilon)
    player2 = QPlayer(mark="O",epsilon = epsilon)
    
    game = Game(root, player1, player2, alpha=a, gamma=g)
    
    for episodes in range(N_episodes):
        game.play()
        game.reset()
    
    Q = game.Q
        
    #filename = "p_files/Q_epsilon_{}_Nepisodes_{}_N_{}_alpha_{}_gamma_{}.p".format(epsilon, N_episodes, N, a, g)
    #pickle.dump(Q, open(filename, "wb"))
    
    
    #Let's compute the Q value    
    #Q = pickle.load(open("p_files/Q_epsilon_{}_Nepisodes_{}_N_{}_alpha_{}_gamma_{}.p".format(epsilon, N_episodes, N, a, g), "rb"))

    x = np.zeros(len(Q))
    catQ = np.zeros(len(Q))
    i=-1
        
    for outer_key, inner_dict in Q.items():
        i = i+1
        #catQ[i] = 0
        #if outer_key.endswith("X"):
            #print("outer_key", outer_key)
        for inner_key, value in inner_dict.items():
            catQ[i] = catQ[i] + value
        x[i] = i

    #    print("q_cat=", catQ)    
    r_sum = 0.0
    r_sum = np.sum(catQ[0:len(Q)])
    #print(catQ,len(catQ))
    Q.clear()
    return r_sum

def train_and_optimize(hyper_config):
    a = hyper_config[0]
    g = hyper_config[1]
    epsilon = hyper_config[2]
    res = -train_Q(a,g,epsilon,N=3,N_episodes=5000)
    return res

hyper_config =[Real(0.01,0.99,name="rate"),
               Real(0.01,0.99,name="discount"),
               Real(0.01,0.99,name="prob")]

res = gp_minimize(train_and_optimize, hyper_config,n_calls=1000,verbose=True,n_random_starts=100)

with open('results_5000_episodes_N_3_1000samples.txt', 'w') as wf:
    wf.write(str(res))
print(res)
