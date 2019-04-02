from board import gameboard
class Cloud:

	def __init__(self,f,l):
		self.x=f
		self.y=l

	def printcloud(self):
		gameboard.board[self.y][self.x]='|'
		gameboard.board[self.y-1][self.x+1]='/'
		gameboard.board[self.y+1][self.x+1]='\\'
		gameboard.board[self.y-2][self.x+2]='/'
		gameboard.board[self.y+2][self.x+2]='\\'
		gameboard.board[self.y-3][self.x+3]='-'
		gameboard.board[self.y+3][self.x+3]='-'
		gameboard.board[self.y+3][self.x+4]='-'
		gameboard.board[self.y-3][self.x+4]='-'
		gameboard.board[self.y+3][self.x+5]='-'
		gameboard.board[self.y-3][self.x+5]='-'
		gameboard.board[self.y-2][self.x+6]='\\'
		gameboard.board[self.y+2][self.x+6]='/'
		gameboard.board[self.y-1][self.x+7]='\\'
		gameboard.board[self.y+1][self.x+7]='/'
		gameboard.board[self.y][self.x+8]='|'
		gameboard.board[self.y][self.x+8]='|'

