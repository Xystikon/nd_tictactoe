import numpy as np
import tkinter as tk
import copy
import pickle as pickle    # cPickle is available in Python 2.x only, otherwise use pickle

from q_learning import Game, HumanPlayer, QPlayer

epsilon = (int(input("Epsilon (in percent): ")))
a = (int(input("Alpha (in percent): ")))
g = (int(input("Gamma (percent): ")))
N_episodes = input("Episodes: ")
N = input("N: ")
Q = pickle.load(open("p_files/Q_epsilon_{}_Nepisodes_{}_N_{}_alpha_{}_gamma_{}.p".format(epsilon, N_episodes, N, a, g), "rb"))

root = tk.Tk()
player1 = HumanPlayer(mark="X")
player2 = QPlayer(mark="O", epsilon=0)

game = Game(root, player1, player2, Q=Q, alpha=a, gamma=g)

game.play()
root.mainloop() 
