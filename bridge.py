from board import Board
from tiles import Tiles
from check import checkboard
from manage import Manage

class Bridge():
	aBridge = []
	vBridge = []
	mark = []
	Bridges = 1
	aBridge.append(257)

	for i in range(0,Bridges):
		vBridge.append(1)

	def moveBridges:
    	for i in range(0,Bridge.Bridges):
            if Bridges.mark[i] == 0:
                if checkboard(self,Bridge.aBridge[i] + Bridge.vBridge[i],28) == 'empty':
                    Board.board[28][Bridge.aBridge[i]]=' ' 
                    Bridge.aBridge[i] = Bridge.aBridge[i] + Bridge.vBridge[i]
                else:
                    Bridge.vBridge[i] = Bridge.vBridge[i]*(-1)

    def printenemies(self):
    	for i in range(0,Bridge.Bridges):
            if Bridge.mark[i] == 0:
                if Bridge.aBridge[i]<Board.st+80 :
                    Board.board[28][Bridge.aBridge[i]]= 'E'

