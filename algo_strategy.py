import gamelib
import random
import math
import numpy as np
#np.set_printoptions(threshold=np.inf)
#from numpy import zeros
import warnings
from sys import maxsize

"""
Most of the algo code you write will be in this file unless you create new
modules yourself. Start by modifying the 'on_turn' function.

Advanced strategy tips: 

Additional functions are made available by importing the AdvancedGameState 
class from gamelib/advanced.py as a replcement for the regular GameState class 
in game.py.

You can analyze action frames by modifying algocore.py.

The GameState.map object can be manually manipulated to create hypothetical 
board states. Though, we recommended making a copy of the map to preserve 
the actual current map state.
all enemy positions:
[[ 13, 27],[ 14, 27],[ 12, 26],[ 13, 26],[ 14, 26],[ 15, 26],[ 11, 25],[ 12, 25],[ 13, 25],[ 14, 25],[ 15, 25],[ 16, 25],[ 10, 24],[ 11, 24],[ 12, 24],[ 13, 24],[ 14, 24],[ 15, 24],[ 16, 24],[ 17, 24],[ 9, 23],[ 10, 23],[ 11, 23],[ 12, 23],[ 13, 23],[ 14, 23],[ 15, 23],[ 16, 23],[ 17, 23],[ 18, 23],[ 8, 22],[ 9, 22],[ 10, 22],[ 11, 22],[ 12, 22],[ 13, 22],[ 14, 22],[ 15, 22],[ 16, 22],[ 17, 22],[ 18, 22],[ 19, 22],[ 7, 21],[ 8, 21],[ 9, 21],[ 10, 21],[ 11, 21],[ 12, 21],[ 13, 21],[ 14, 21],[ 15, 21],[ 16, 21],[ 17, 21],[ 18, 21],[ 19, 21],[ 20, 21],[ 6, 20],[ 7, 20],[ 8, 20],[ 9, 20],[ 10, 20],[ 11, 20],[ 12, 20],[ 13, 20],[ 14, 20],[ 15, 20],[ 16, 20],[ 17, 20],[ 18, 20],[ 19, 20],[ 20, 20],[ 21, 20],[ 5, 19],[ 6, 19],[ 7, 19],[ 8, 19],[ 9, 19],[ 10, 19],[ 11, 19],[ 12, 19],[ 13, 19],[ 14, 19],[ 15, 19],[ 16, 19],[ 17, 19],[ 18, 19],[ 19, 19],[ 20, 19],[ 21, 19],[ 22, 19],[ 4, 18],[ 5, 18],[ 6, 18],[ 7, 18],[ 8, 18],[ 9, 18],[ 10, 18],[ 11, 18],[ 12, 18],[ 13, 18],[ 14, 18],[ 15, 18],[ 16, 18],[ 17, 18],[ 18, 18],[ 19, 18],[ 20, 18],[ 21, 18],[ 22, 18],[ 23, 18],[ 3, 17],[ 4, 17],[ 5, 17],[ 6, 17],[ 7, 17],[ 8, 17],[ 9, 17],[ 10, 17],[ 11, 17],[ 12, 17],[ 13, 17],[ 14, 17],[ 15, 17],[ 16, 17],[ 17, 17],[ 18, 17],[ 19, 17],[ 20, 17],[ 21, 17],[ 22, 17],[ 23, 17],[ 24, 17],[ 2, 16],[ 3, 16],[ 4, 16],[ 5, 16],[ 6, 16],[ 7, 16],[ 8, 16],[ 9, 16],[ 10, 16],[ 11, 16],[ 12, 16],[ 13, 16],[ 14, 16],[ 15, 16],[ 16, 16],[ 17, 16],[ 18, 16],[ 19, 16],[ 20, 16],[ 21, 16],[ 22, 16],[ 23, 16],[ 24, 16],[ 25, 16],[ 1, 15],[ 2, 15],[ 3, 15],[ 4, 15],[ 5, 15],[ 6, 15],[ 7, 15],[ 8, 15],[ 9, 15],[ 10, 15],[ 11, 15],[ 12, 15],[ 13, 15],[ 14, 15],[ 15, 15],[ 16, 15],[ 17, 15],[ 18, 15],[ 19, 15],[ 20, 15],[ 21, 15],[ 22, 15],[ 23, 15],[ 24, 15],[ 25, 15],[ 26, 15],[ 0, 14],[ 1, 14],[ 2, 14],[ 3, 14],[ 4, 14],[ 5, 14],[ 6, 14],[ 7, 14],[ 8, 14],[ 9, 14],[ 10, 14],[ 11, 14],[ 12, 14],[ 13, 14],[ 14, 14],[ 15, 14],[ 16, 14],[ 17, 14],[ 18, 14],[ 19, 14],[ 20, 14],[ 21, 14],[ 22, 14],[ 23, 14],[ 24, 14],[ 25, 14],[ 26, 14],[ 27, 14]]
all my positions:
[[ 0, 13],[ 1, 13],[ 2, 13],[ 3, 13],[ 4, 13],[ 5, 13],[ 6, 13],[ 7, 13],[ 8, 13],[ 9, 13],[ 10, 13],[ 11, 13],[ 12, 13],[ 13, 13],[ 14, 13],[ 15, 13],[ 16, 13],[ 17, 13],[ 18, 13],[ 19, 13],[ 20, 13],[ 21, 13],[ 22, 13],[ 23, 13],[ 24, 13],[ 25, 13],[ 26, 13],[ 27, 13],[ 1, 12],[ 2, 12],[ 3, 12],[ 4, 12],[ 5, 12],[ 6, 12],[ 7, 12],[ 8, 12],[ 9, 12],[ 10, 12],[ 11, 12],[ 12, 12],[ 13, 12],[ 14, 12],[ 15, 12],[ 16, 12],[ 17, 12],[ 18, 12],[ 19, 12],[ 20, 12],[ 21, 12],[ 22, 12],[ 23, 12],[ 24, 12],[ 25, 12],[ 26, 12],[ 2, 11],[ 3, 11],[ 4, 11],[ 5, 11],[ 6, 11],[ 7, 11],[ 8, 11],[ 9, 11],[ 10, 11],[ 11, 11],[ 12, 11],[ 13, 11],[ 14, 11],[ 15, 11],[ 16, 11],[ 17, 11],[ 18, 11],[ 19, 11],[ 20, 11],[ 21, 11],[ 22, 11],[ 23, 11],[ 24, 11],[ 25, 11],[ 3, 10],[ 4, 10],[ 5, 10],[ 6, 10],[ 7, 10],[ 8, 10],[ 9, 10],[ 10, 10],[ 11, 10],[ 12, 10],[ 13, 10],[ 14, 10],[ 15, 10],[ 16, 10],[ 17, 10],[ 18, 10],[ 19, 10],[ 20, 10],[ 21, 10],[ 22, 10],[ 23, 10],[ 24, 10],[ 4, 9],[ 5, 9],[ 6, 9],[ 7, 9],[ 8, 9],[ 9, 9],[ 10, 9],[ 11, 9],[ 12, 9],[ 13, 9],[ 14, 9],[ 15, 9],[ 16, 9],[ 17, 9],[ 18, 9],[ 19, 9],[ 20, 9],[ 21, 9],[ 22, 9],[ 23, 9],[ 5, 8],[ 6, 8],[ 7, 8],[ 8, 8],[ 9, 8],[ 10, 8],[ 11, 8],[ 12, 8],[ 13, 8],[ 14, 8],[ 15, 8],[ 16, 8],[ 17, 8],[ 18, 8],[ 19, 8],[ 20, 8],[ 21, 8],[ 22, 8],[ 6, 7],[ 7, 7],[ 8, 7],[ 9, 7],[ 10, 7],[ 11, 7],[ 12, 7],[ 13, 7],[ 14, 7],[ 15, 7],[ 16, 7],[ 17, 7],[ 18, 7],[ 19, 7],[ 20, 7],[ 21, 7],[ 7, 6],[ 8, 6],[ 9, 6],[ 10, 6],[ 11, 6],[ 12, 6],[ 13, 6],[ 14, 6],[ 15, 6],[ 16, 6],[ 17, 6],[ 18, 6],[ 19, 6],[ 20, 6],[ 8, 5],[ 9, 5],[ 10, 5],[ 11, 5],[ 12, 5],[ 13, 5],[ 14, 5],[ 15, 5],[ 16, 5],[ 17, 5],[ 18, 5],[ 19, 5],[ 9, 4],[ 10, 4],[ 11, 4],[ 12, 4],[ 13, 4],[ 14, 4],[ 15, 4],[ 16, 4],[ 17, 4],[ 18, 4],[ 10, 3],[ 11, 3],[ 12, 3],[ 13, 3],[ 14, 3],[ 15, 3],[ 16, 3],[ 17, 3],[ 11, 2],[ 12, 2],[ 13, 2],[ 14, 2],[ 15, 2],[ 16, 2],[ 12, 1],[ 13, 1],[ 14, 1],[ 15, 1],[ 13, 0],[ 14, 0]]
my edge positions:
[[ 0, 13],[ 27, 13],[ 1, 12],[ 26, 12],[ 2, 11],[ 25, 11],[ 3, 10],[ 24, 10],[ 4, 9],[ 23, 9],[ 5, 8],[ 22, 8],[ 6, 7],[ 21, 7],[ 7, 6],[ 20, 6],[ 8, 5],[ 19, 5],[ 9, 4],[ 18, 4],[ 10, 3],[ 17, 3],[ 11, 2],[ 16, 2],[ 12, 1],[ 15, 1],[ 13, 0],[ 14, 0]]
"""

class AlgoStrategy(gamelib.AlgoCore):
    def __init__(self):
        super().__init__()
        random.seed()




    
    def zrs(self,dims):
        ret = []
        if len(dims) == 1:
            while len(ret) < dims[0]:
                ret.append(0)
        else:
            while len(ret) < dims[0]:
                ret.append(zrs(dims[1:]))
        return ret
    
    
    def on_game_start(self, config):
        """ 
        Read in config and perform any initial setup here 
        """
        gamelib.debug_write('Configuring your custom algo strategy...')
        self.config = config
        global FILTER, ENCRYPTOR, DESTRUCTOR, PING, EMP, SCRAMBLER
        FILTER = config["unitInformation"][0]["shorthand"]
        ENCRYPTOR = config["unitInformation"][1]["shorthand"]
        DESTRUCTOR = config["unitInformation"][2]["shorthand"]
        PING = config["unitInformation"][3]["shorthand"]
        EMP = config["unitInformation"][4]["shorthand"]
        SCRAMBLER = config["unitInformation"][5]["shorthand"]
        
        global all_pos
        all_pos = [[ 0, 13],[ 1, 13],[ 2, 13],[ 3, 13],[ 4, 13],[ 5, 13],[ 6, 13],[ 7, 13],[ 8, 13],[ 9, 13],[ 10, 13],[ 11, 13],[ 12, 13],[ 13, 13],[ 14, 13],[ 15, 13],[ 16, 13],[ 17, 13],[ 18, 13],[ 19, 13],[ 20, 13],[ 21, 13],[ 22, 13],[ 23, 13],[ 24, 13],[ 25, 13],[ 26, 13],[ 27, 13],[ 1, 12],[ 2, 12],[ 3, 12],[ 4, 12],[ 5, 12],[ 6, 12],[ 7, 12],[ 8, 12],[ 9, 12],[ 10, 12],[ 11, 12],[ 12, 12],[ 13, 12],[ 14, 12],[ 15, 12],[ 16, 12],[ 17, 12],[ 18, 12],[ 19, 12],[ 20, 12],[ 21, 12],[ 22, 12],[ 23, 12],[ 24, 12],[ 25, 12],[ 26, 12],[ 2, 11],[ 3, 11],[ 4, 11],[ 5, 11],[ 6, 11],[ 7, 11],[ 8, 11],[ 9, 11],[ 10, 11],[ 11, 11],[ 12, 11],[ 13, 11],[ 14, 11],[ 15, 11],[ 16, 11],[ 17, 11],[ 18, 11],[ 19, 11],[ 20, 11],[ 21, 11],[ 22, 11],[ 23, 11],[ 24, 11],[ 25, 11],[ 3, 10],[ 4, 10],[ 5, 10],[ 6, 10],[ 7, 10],[ 8, 10],[ 9, 10],[ 10, 10],[ 11, 10],[ 12, 10],[ 13, 10],[ 14, 10],[ 15, 10],[ 16, 10],[ 17, 10],[ 18, 10],[ 19, 10],[ 20, 10],[ 21, 10],[ 22, 10],[ 23, 10],[ 24, 10],[ 4, 9],[ 5, 9],[ 6, 9],[ 7, 9],[ 8, 9],[ 9, 9],[ 10, 9],[ 11, 9],[ 12, 9],[ 13, 9],[ 14, 9],[ 15, 9],[ 16, 9],[ 17, 9],[ 18, 9],[ 19, 9],[ 20, 9],[ 21, 9],[ 22, 9],[ 23, 9],[ 5, 8],[ 6, 8],[ 7, 8],[ 8, 8],[ 9, 8],[ 10, 8],[ 11, 8],[ 12, 8],[ 13, 8],[ 14, 8],[ 15, 8],[ 16, 8],[ 17, 8],[ 18, 8],[ 19, 8],[ 20, 8],[ 21, 8],[ 22, 8],[ 6, 7],[ 7, 7],[ 8, 7],[ 9, 7],[ 10, 7],[ 11, 7],[ 12, 7],[ 13, 7],[ 14, 7],[ 15, 7],[ 16, 7],[ 17, 7],[ 18, 7],[ 19, 7],[ 20, 7],[ 21, 7],[ 7, 6],[ 8, 6],[ 9, 6],[ 10, 6],[ 11, 6],[ 12, 6],[ 13, 6],[ 14, 6],[ 15, 6],[ 16, 6],[ 17, 6],[ 18, 6],[ 19, 6],[ 20, 6],[ 8, 5],[ 9, 5],[ 10, 5],[ 11, 5],[ 12, 5],[ 13, 5],[ 14, 5],[ 15, 5],[ 16, 5],[ 17, 5],[ 18, 5],[ 19, 5],[ 9, 4],[ 10, 4],[ 11, 4],[ 12, 4],[ 13, 4],[ 14, 4],[ 15, 4],[ 16, 4],[ 17, 4],[ 18, 4],[ 10, 3],[ 11, 3],[ 12, 3],[ 13, 3],[ 14, 3],[ 15, 3],[ 16, 3],[ 17, 3],[ 11, 2],[ 12, 2],[ 13, 2],[ 14, 2],[ 15, 2],[ 16, 2],[ 12, 1],[ 13, 1],[ 14, 1],[ 15, 1],[ 13, 0],[ 14, 0],[ 13, 27],[ 14, 27],[ 12, 26],[ 13, 26],[ 14, 26],[ 15, 26],[ 11, 25],[ 12, 25],[ 13, 25],[ 14, 25],[ 15, 25],[ 16, 25],[ 10, 24],[ 11, 24],[ 12, 24],[ 13, 24],[ 14, 24],[ 15, 24],[ 16, 24],[ 17, 24],[ 9, 23],[ 10, 23],[ 11, 23],[ 12, 23],[ 13, 23],[ 14, 23],[ 15, 23],[ 16, 23],[ 17, 23],[ 18, 23],[ 8, 22],[ 9, 22],[ 10, 22],[ 11, 22],[ 12, 22],[ 13, 22],[ 14, 22],[ 15, 22],[ 16, 22],[ 17, 22],[ 18, 22],[ 19, 22],[ 7, 21],[ 8, 21],[ 9, 21],[ 10, 21],[ 11, 21],[ 12, 21],[ 13, 21],[ 14, 21],[ 15, 21],[ 16, 21],[ 17, 21],[ 18, 21],[ 19, 21],[ 20, 21],[ 6, 20],[ 7, 20],[ 8, 20],[ 9, 20],[ 10, 20],[ 11, 20],[ 12, 20],[ 13, 20],[ 14, 20],[ 15, 20],[ 16, 20],[ 17, 20],[ 18, 20],[ 19, 20],[ 20, 20],[ 21, 20],[ 5, 19],[ 6, 19],[ 7, 19],[ 8, 19],[ 9, 19],[ 10, 19],[ 11, 19],[ 12, 19],[ 13, 19],[ 14, 19],[ 15, 19],[ 16, 19],[ 17, 19],[ 18, 19],[ 19, 19],[ 20, 19],[ 21, 19],[ 22, 19],[ 4, 18],[ 5, 18],[ 6, 18],[ 7, 18],[ 8, 18],[ 9, 18],[ 10, 18],[ 11, 18],[ 12, 18],[ 13, 18],[ 14, 18],[ 15, 18],[ 16, 18],[ 17, 18],[ 18, 18],[ 19, 18],[ 20, 18],[ 21, 18],[ 22, 18],[ 23, 18],[ 3, 17],[ 4, 17],[ 5, 17],[ 6, 17],[ 7, 17],[ 8, 17],[ 9, 17],[ 10, 17],[ 11, 17],[ 12, 17],[ 13, 17],[ 14, 17],[ 15, 17],[ 16, 17],[ 17, 17],[ 18, 17],[ 19, 17],[ 20, 17],[ 21, 17],[ 22, 17],[ 23, 17],[ 24, 17],[ 2, 16],[ 3, 16],[ 4, 16],[ 5, 16],[ 6, 16],[ 7, 16],[ 8, 16],[ 9, 16],[ 10, 16],[ 11, 16],[ 12, 16],[ 13, 16],[ 14, 16],[ 15, 16],[ 16, 16],[ 17, 16],[ 18, 16],[ 19, 16],[ 20, 16],[ 21, 16],[ 22, 16],[ 23, 16],[ 24, 16],[ 25, 16],[ 1, 15],[ 2, 15],[ 3, 15],[ 4, 15],[ 5, 15],[ 6, 15],[ 7, 15],[ 8, 15],[ 9, 15],[ 10, 15],[ 11, 15],[ 12, 15],[ 13, 15],[ 14, 15],[ 15, 15],[ 16, 15],[ 17, 15],[ 18, 15],[ 19, 15],[ 20, 15],[ 21, 15],[ 22, 15],[ 23, 15],[ 24, 15],[ 25, 15],[ 26, 15],[ 0, 14],[ 1, 14],[ 2, 14],[ 3, 14],[ 4, 14],[ 5, 14],[ 6, 14],[ 7, 14],[ 8, 14],[ 9, 14],[ 10, 14],[ 11, 14],[ 12, 14],[ 13, 14],[ 14, 14],[ 15, 14],[ 16, 14],[ 17, 14],[ 18, 14],[ 19, 14],[ 20, 14],[ 21, 14],[ 22, 14],[ 23, 14],[ 24, 14],[ 25, 14],[ 26, 14],[ 27, 14]]
        global all_enemy_pos
        all_enemy_pos = [[ 13, 27],[ 14, 27],[ 12, 26],[ 13, 26],[ 14, 26],[ 15, 26],[ 11, 25],[ 12, 25],[ 13, 25],[ 14, 25],[ 15, 25],[ 16, 25],[ 10, 24],[ 11, 24],[ 12, 24],[ 13, 24],[ 14, 24],[ 15, 24],[ 16, 24],[ 17, 24],[ 9, 23],[ 10, 23],[ 11, 23],[ 12, 23],[ 13, 23],[ 14, 23],[ 15, 23],[ 16, 23],[ 17, 23],[ 18, 23],[ 8, 22],[ 9, 22],[ 10, 22],[ 11, 22],[ 12, 22],[ 13, 22],[ 14, 22],[ 15, 22],[ 16, 22],[ 17, 22],[ 18, 22],[ 19, 22],[ 7, 21],[ 8, 21],[ 9, 21],[ 10, 21],[ 11, 21],[ 12, 21],[ 13, 21],[ 14, 21],[ 15, 21],[ 16, 21],[ 17, 21],[ 18, 21],[ 19, 21],[ 20, 21],[ 6, 20],[ 7, 20],[ 8, 20],[ 9, 20],[ 10, 20],[ 11, 20],[ 12, 20],[ 13, 20],[ 14, 20],[ 15, 20],[ 16, 20],[ 17, 20],[ 18, 20],[ 19, 20],[ 20, 20],[ 21, 20],[ 5, 19],[ 6, 19],[ 7, 19],[ 8, 19],[ 9, 19],[ 10, 19],[ 11, 19],[ 12, 19],[ 13, 19],[ 14, 19],[ 15, 19],[ 16, 19],[ 17, 19],[ 18, 19],[ 19, 19],[ 20, 19],[ 21, 19],[ 22, 19],[ 4, 18],[ 5, 18],[ 6, 18],[ 7, 18],[ 8, 18],[ 9, 18],[ 10, 18],[ 11, 18],[ 12, 18],[ 13, 18],[ 14, 18],[ 15, 18],[ 16, 18],[ 17, 18],[ 18, 18],[ 19, 18],[ 20, 18],[ 21, 18],[ 22, 18],[ 23, 18],[ 3, 17],[ 4, 17],[ 5, 17],[ 6, 17],[ 7, 17],[ 8, 17],[ 9, 17],[ 10, 17],[ 11, 17],[ 12, 17],[ 13, 17],[ 14, 17],[ 15, 17],[ 16, 17],[ 17, 17],[ 18, 17],[ 19, 17],[ 20, 17],[ 21, 17],[ 22, 17],[ 23, 17],[ 24, 17],[ 2, 16],[ 3, 16],[ 4, 16],[ 5, 16],[ 6, 16],[ 7, 16],[ 8, 16],[ 9, 16],[ 10, 16],[ 11, 16],[ 12, 16],[ 13, 16],[ 14, 16],[ 15, 16],[ 16, 16],[ 17, 16],[ 18, 16],[ 19, 16],[ 20, 16],[ 21, 16],[ 22, 16],[ 23, 16],[ 24, 16],[ 25, 16],[ 1, 15],[ 2, 15],[ 3, 15],[ 4, 15],[ 5, 15],[ 6, 15],[ 7, 15],[ 8, 15],[ 9, 15],[ 10, 15],[ 11, 15],[ 12, 15],[ 13, 15],[ 14, 15],[ 15, 15],[ 16, 15],[ 17, 15],[ 18, 15],[ 19, 15],[ 20, 15],[ 21, 15],[ 22, 15],[ 23, 15],[ 24, 15],[ 25, 15],[ 26, 15],[ 0, 14],[ 1, 14],[ 2, 14],[ 3, 14],[ 4, 14],[ 5, 14],[ 6, 14],[ 7, 14],[ 8, 14],[ 9, 14],[ 10, 14],[ 11, 14],[ 12, 14],[ 13, 14],[ 14, 14],[ 15, 14],[ 16, 14],[ 17, 14],[ 18, 14],[ 19, 14],[ 20, 14],[ 21, 14],[ 22, 14],[ 23, 14],[ 24, 14],[ 25, 14],[ 26, 14],[ 27, 14]]
        global all_my_pos
        all_my_pos = [[ 0, 13],[ 1, 13],[ 2, 13],[ 3, 13],[ 4, 13],[ 5, 13],[ 6, 13],[ 7, 13],[ 8, 13],[ 9, 13],[ 10, 13],[ 11, 13],[ 12, 13],[ 13, 13],[ 14, 13],[ 15, 13],[ 16, 13],[ 17, 13],[ 18, 13],[ 19, 13],[ 20, 13],[ 21, 13],[ 22, 13],[ 23, 13],[ 24, 13],[ 25, 13],[ 26, 13],[ 27, 13],[ 1, 12],[ 2, 12],[ 3, 12],[ 4, 12],[ 5, 12],[ 6, 12],[ 7, 12],[ 8, 12],[ 9, 12],[ 10, 12],[ 11, 12],[ 12, 12],[ 13, 12],[ 14, 12],[ 15, 12],[ 16, 12],[ 17, 12],[ 18, 12],[ 19, 12],[ 20, 12],[ 21, 12],[ 22, 12],[ 23, 12],[ 24, 12],[ 25, 12],[ 26, 12],[ 2, 11],[ 3, 11],[ 4, 11],[ 5, 11],[ 6, 11],[ 7, 11],[ 8, 11],[ 9, 11],[ 10, 11],[ 11, 11],[ 12, 11],[ 13, 11],[ 14, 11],[ 15, 11],[ 16, 11],[ 17, 11],[ 18, 11],[ 19, 11],[ 20, 11],[ 21, 11],[ 22, 11],[ 23, 11],[ 24, 11],[ 25, 11],[ 3, 10],[ 4, 10],[ 5, 10],[ 6, 10],[ 7, 10],[ 8, 10],[ 9, 10],[ 10, 10],[ 11, 10],[ 12, 10],[ 13, 10],[ 14, 10],[ 15, 10],[ 16, 10],[ 17, 10],[ 18, 10],[ 19, 10],[ 20, 10],[ 21, 10],[ 22, 10],[ 23, 10],[ 24, 10],[ 4, 9],[ 5, 9],[ 6, 9],[ 7, 9],[ 8, 9],[ 9, 9],[ 10, 9],[ 11, 9],[ 12, 9],[ 13, 9],[ 14, 9],[ 15, 9],[ 16, 9],[ 17, 9],[ 18, 9],[ 19, 9],[ 20, 9],[ 21, 9],[ 22, 9],[ 23, 9],[ 5, 8],[ 6, 8],[ 7, 8],[ 8, 8],[ 9, 8],[ 10, 8],[ 11, 8],[ 12, 8],[ 13, 8],[ 14, 8],[ 15, 8],[ 16, 8],[ 17, 8],[ 18, 8],[ 19, 8],[ 20, 8],[ 21, 8],[ 22, 8],[ 6, 7],[ 7, 7],[ 8, 7],[ 9, 7],[ 10, 7],[ 11, 7],[ 12, 7],[ 13, 7],[ 14, 7],[ 15, 7],[ 16, 7],[ 17, 7],[ 18, 7],[ 19, 7],[ 20, 7],[ 21, 7],[ 7, 6],[ 8, 6],[ 9, 6],[ 10, 6],[ 11, 6],[ 12, 6],[ 13, 6],[ 14, 6],[ 15, 6],[ 16, 6],[ 17, 6],[ 18, 6],[ 19, 6],[ 20, 6],[ 8, 5],[ 9, 5],[ 10, 5],[ 11, 5],[ 12, 5],[ 13, 5],[ 14, 5],[ 15, 5],[ 16, 5],[ 17, 5],[ 18, 5],[ 19, 5],[ 9, 4],[ 10, 4],[ 11, 4],[ 12, 4],[ 13, 4],[ 14, 4],[ 15, 4],[ 16, 4],[ 17, 4],[ 18, 4],[ 10, 3],[ 11, 3],[ 12, 3],[ 13, 3],[ 14, 3],[ 15, 3],[ 16, 3],[ 17, 3],[ 11, 2],[ 12, 2],[ 13, 2],[ 14, 2],[ 15, 2],[ 16, 2],[ 12, 1],[ 13, 1],[ 14, 1],[ 15, 1],[ 13, 0],[ 14, 0]]
        global my_edge_pos
        my_edge_pos = [[ 0, 13],[ 27, 13],[ 1, 12],[ 26, 12],[ 2, 11],[ 25, 11],[ 3, 10],[ 24, 10],[ 4, 9],[ 23, 9],[ 5, 8],[ 22, 8],[ 6, 7],[ 21, 7],[ 7, 6],[ 20, 6],[ 8, 5],[ 19, 5],[ 9, 4],[ 18, 4],[ 10, 3],[ 17, 3],[ 11, 2],[ 16, 2],[ 12, 1],[ 15, 1],[ 13, 0],[ 14, 0]]
    
    
    def on_turn(self, turn_state):
        """
        This function is called every turn with the game state wrapper as
        an argument. The wrapper stores the state of the arena and has methods
        for querying its state, allocating your current resources as planned
        unit deployments, and transmitting your intended deployments to the
        game engine.
        """
        game_state = gamelib.GameState(self.config, turn_state)
        gamelib.debug_write('Performing turn {} of your custom algo strategy'.format(game_state.turn_number))
        #game_state.suppress_warnings(True)  #Uncomment this line to suppress warnings
        self.test_strategy(game_state)
        game_state.submit_turn()
    
    
    
    
    def zrs(self,dims):
        ret = []
        if len(dims) == 1:
            while len(ret) < dims[0]:
                ret.append(0)
        else:
            while len(ret) < dims[0]:
                ret.append(self.zrs(dims[1:]))
        return ret
    
    def cpmat(self,m,dp):
        ret = []
        if dp == 1:
            for x in m:
                ret.append(x)
        else:
            for l in m:
              ret.append(self.cpmat(l,dp-1))
        return ret
    
    
    
    def state_matrix(self, game_state):
        state_mat = []
        state_mat = self.zrs([3,28,28])
        #used_pos = []
        #np.save('/home/moritz/Documents/C1GamesStarterKit-master/algos/rating-algo/state_mat',state_mat)
        for pos in all_pos:
            #if pos in used_pos:
                #print('pos_doppelt')
            #used_pos.append(pos)
            units = game_state.game_map[pos[0],pos[1]]
            for unit in units:
                #print(unit,units,state_mat[0][pos[0]][pos[1]],state_mat[1][pos[0]][pos[1]],state_mat[2][pos[0]][pos[1]])
                if unit.unit_type == 'FF':
                    #if state_mat[0][pos[0]][pos[1]] > 0:
                    #    print(unit.unit_type,pos,state_mat[0][pos[0]][pos[1]],units,0.5 + 0.5*unit.stability/unit.max_stability)
                    state_mat[0][pos[0]][pos[1]] = state_mat[0][pos[0]][pos[1]] + 0.5 + 0.5*unit.stability/unit.max_stability
                elif unit.unit_type == 'EF':
                    #if state_mat[0][pos[0]][pos[1]] > 0:
                    #    print(unit.unit_type,pos,state_mat[1][pos[0]][pos[1]],units,0.5 + 0.5*unit.stability/unit.max_stability)
                    state_mat[1][pos[0]][pos[1]] = state_mat[1][pos[0]][pos[1]] + 0.5 + 0.5*unit.stability/unit.max_stability
                elif unit.unit_type == 'DF':
                    #if state_mat[0][pos[0]][pos[1]] > 0:
                    #    print(unit.unit_type,pos,state_mat[2][pos[0]][pos[1]],units,0.5 + 0.5*unit.stability/unit.max_stability)
                    state_mat[2][pos[0]][pos[1]] = state_mat[2][pos[0]][pos[1]] + 0.5 + 0.5*unit.stability/unit.max_stability
                #print(unit,units,state_mat[0][pos[0]][pos[1]],state_mat[1][pos[0]][pos[1]],state_mat[2][pos[0]][pos[1]])
                #else:
                    #print('Some thing wong with state_matrix')
                
        #np.save('/home/moritz/Documents/C1GamesStarterKit-master/algos/rating-algo/state_mat',state_mat)
        return state_mat
        
    
    def info_vector(self, game_state):
        info_vec = []
        info_vec = self.zrs([3,28])
        
        for pos in my_edge_pos:
            units = game_state.game_map[pos[0],pos[1]]
            for unit in units:
                #print(unit.unit_type)
                if unit.unit_type == 'PI':
                    info_vec[0][pos[0]] = info_vec[0][pos[0]] + 0.5 + 0.5*unit.stability/unit.max_stability
                elif unit.unit_type == 'EI':
                    info_vec[1][pos[0]] = info_vec[1][pos[0]] + 0.5 + 0.5*unit.stability/unit.max_stability
                elif unit.unit_type == 'SI':
                    info_vec[2][pos[0]] = info_vec[2][pos[0]] + 0.5 + 0.5*unit.stability/unit.max_stability
                    
        #np.save('/home/moritz/Documents/C1GamesStarterKit-master/algos/rating-algo/vec.dat',info_vec)
        return info_vec
    
    def nxt_moves(self, game_state, state_mat, info_vec):
        nxt_mvs = []
        new_state_mat = self.cpmat(state_mat,3)
        new_info_vec = self.cpmat(info_vec,2)
        #print(info_vec)
        '''
        for pos in all_my_pos:
            if game_state.can_spawn(FILTER,pos):
                new_state_mat[0][pos[0]][pos[1]] = state_mat[0][pos[0]][pos[1]] + 1
                nxt_mvs.append([self.cpmat(new_state_mat,3),self.cpmat(info_vec,2),pos,FILTER])
            
            if game_state.can_spawn(ENCRYPTOR,pos):
                new_state_mat[1][pos[0]][pos[1]] = state_mat[1][pos[0]][pos[1]] + 1
                nxt_mvs.append([self.cpmat(new_state_mat,3),self.cpmat(info_vec,2),pos,ENCRYPTOR])
            
            if game_state.can_spawn(DESTRUCTOR,pos):
                new_state_mat[2][pos[0]][pos[1]] = state_mat[2][pos[0]][pos[1]] + 1
                nxt_mvs.append([self.cpmat(new_state_mat,3),self.cpmat(info_vec,2),pos,DESTRUCTOR])
            '''
        
        for pos in my_edge_pos:
            if game_state.can_spawn(PING,pos):
                new_info_vec[0][pos[0]] = info_vec[0][pos[0]] + 1
                nxt_mvs.append([self.cpmat(state_mat,3),self.cpmat(new_info_vec,2),pos,PING])
            
            if game_state.can_spawn(EMP,pos):
                new_info_vec[1][pos[0]] = info_vec[1][pos[0]] + 1
                nxt_mvs.append([self.cpmat(state_mat,3),self.cpmat(new_info_vec,2),pos,EMP])
            
            if game_state.can_spawn(SCRAMBLER,pos):
                new_info_vec[2][pos[0]] = info_vec[2][pos[0]] + 1
                nxt_mvs.append([self.cpmat(state_mat,3),self.cpmat(new_info_vec,2),pos,SCRAMBLER])
            #print(info_vec)
        return nxt_mvs
    
    
    def r8gr8(self,state_mat,info_vec,game_state):
        state_vec = []
        for pos in all_pos:
            for t in range(0,3):
                state_vec.append(state_mat[t][pos[0]][pos[1]])
        
        state_vec = state_vec + info_vec[0] + info_vec[1] + info_vec[2]
        
        state_vec.append(game_state.get_resource(game_state.CORES,0))
        state_vec.append(game_state.get_resource(game_state.CORES,1))
        state_vec.append(game_state.get_resource(game_state.BITS,0))
        state_vec.append(game_state.get_resource(game_state.BITS,1))
        #print(state_vec)
        return random.randint(-100,100)
        
       
        
    
    def softmax(self,r8ed):
        enum = 0.0
        for x in r8ed:
            enum = enum + math.exp(x)
            
        ret = []
        
        for x in r8ed:
            ret.append(math.exp(x)/enum)
            
        return ret
        
    
    def pick_w8ed(self,weights):
        r = random.random()
        s = 0.0
        #weiths = weights / sum(weights)
        i = -1
        while s < r and i < len(weights) - 1:
            i = i + 1
            s = s + weights[i]
            
        if i < 0:
            i = 0
            
        
        return i
    
    def test_strategy(self, game_state):
        
        
        
        '''
        for pos in all_my_pos:
            if not game_state.can_spawn(FILTER,pos):
                print("something is up with FILTER")
                print(pos)
        for pos in my_edge_pos:
            if not game_state.can_spawn(PING,pos):
                print("something is up with PING")
                print(pos)
            
    	'''
    	
        '''
        rpos = all_my_pos[random.randint(0,len(all_my_pos) - 1)]
        while game_state.can_spawn(FILTER,rpos):
            game_state.attempt_spawn(FILTER,rpos)
            rpos = all_my_pos[random.randint(0, len(all_my_pos) - 1)]
        
        
        
        rpos = my_edge_pos[random.randint(0,len(my_edge_pos) - 1)]
        while game_state.can_spawn(PING,rpos):
            game_state.attempt_spawn(PING,rpos)
            rpos = my_edge_pos[random.randint(0, len(my_edge_pos) - 1)]
        '''
        
        state_mat = self.state_matrix(game_state)
        #print(state_mat)
        info_vec = self.info_vector(game_state)
        print(info_vec)
        nxt_mvs = self.nxt_moves(game_state, state_mat, info_vec)
        np.save('/home/moritz/Documents/C1GamesStarterKit-master/algos/rating-algo/nxt',nxt_mvs)
        
        weights = []
        for st in nxt_mvs:
            weights.append(self.r8gr8(st[0],st[1],game_state))
            
        weights = self.softmax(weights)
        
        ind = self.pick_w8ed(weights)
        
        #print(max(weights))
        
        
        while not ind == len(nxt_mvs):
            game_state.attempt_spawn(nxt_mvs[ind][3],nxt_mvs[ind][2])
            state_mat = self.state_matrix(game_state)
            info_vec = self.info_vector(game_state)
            nxt_mvs = self.nxt_moves(game_state, state_mat, info_vec)
            
            weights = []
            for st in nxt_mvs:
                weights.append(self.r8gr8(st[0],st[1],game_state))
            weights = self.softmax(weights)
            ind = self.pick_w8ed(weights)
            
        print(info_vec)

if __name__ == "__main__":
    algo = AlgoStrategy()
    algo.start()
