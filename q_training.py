import numpy as np
import tkinter as tk
import copy
import pickle
from Q_Learning_ndgame import Game, QPlayer     # Classes used for Tic Tac Toe

root = tk.Tk()
epsilon = 0.9
player1 = QPlayer(mark="X",epsilon = epsilon)
player2 = QPlayer(mark="O",epsilon = epsilon)
game = Game(root, player1, player2)

N_episodes = 10000
N = 3
for episodes in range(N_episodes):
    game.play()
    game.reset()

Q = game.Q

filename = "Q_epsilon_09_Nepisodes_{}_N={}.p".format(N_episodes, N)
pickle.dump(Q, open(p_files/filename, "wb"))
