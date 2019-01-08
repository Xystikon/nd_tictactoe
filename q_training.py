import numpy as np
import tkinter as tk
import copy
import pickle
from q_learning import Game, QPlayer     # Classes used for Tic Tac Toe
#import shutil

root = tk.Tk()
epsilon = (int(input("Epsilon (percent): ")))/100
player1 = QPlayer(mark="X",epsilon = epsilon)
player2 = QPlayer(mark="O",epsilon = epsilon)

a = (int(input("Alpha (percent): ")))/100
g = (int(input("Gamma (percent): ")))/100

game = Game(root, player1, player2, alpha=a, gamma=g)

N_episodes = int(input("Episodes: "))
N = int(input("N: "))
print(N_episodes, N)
for episodes in range(N_episodes):
    game.play()
    game.reset()

Q = game.Q

filename = "p_files/Q_epsilon_{}_Nepisodes_{}_N_{}_alpha_{}_gamma_{}.p".format(epsilon, N_episodes, N, a, g)
pickle.dump(Q, open(filename, "wb"))

#source = '/home/michoski/ndgame/nd_tictactoe/'
#destination = '/home/michoski/ndgame/nd_tictactoe/p_files/'

#shutil.move(source+filename,destination)
