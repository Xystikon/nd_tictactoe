import numpy as np
import tkinter as tk
import copy
import pickle
from q_learning import Game, QPlayer     # Classes used for Tic Tac Toe
#import shutil

root = tk.Tk()
epsilon = 0.9
player1 = QPlayer(mark="X",epsilon = epsilon)
player2 = QPlayer(mark="O",epsilon = epsilon)
game = Game(root, player1, player2)

N_episodes = 10
N = 3
for episodes in range(N_episodes):
    game.play()
    game.reset()

Q = game.Q

filename = "p_files/Q_epsilon_09_Nepisodes_{}_N_{}.p".format(N_episodes, N)
pickle.dump(Q, open(filename, "wb"))

#source = '/home/michoski/ndgame/nd_tictactoe/'
#destination = '/home/michoski/ndgame/nd_tictactoe/p_files/'

#shutil.move(source+filename,destination)
