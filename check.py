''' The Check function is an independent
# funciton that returns what is there
# at a specific position.'''

from board import gameboard


def checkboard(self, alpha, beta):
    ''' checks board for what's at position'''
    if  beta > 31 or alpha > 400:
        return 'wall'

    if gameboard.board[beta][alpha] == '\\' or gameboard.board[beta][alpha] == '_' or gameboard.board[beta][alpha] == '/':
        return 'boss'


    if gameboard.board[beta][alpha] == 'T':
    	return 'mario'
    	
    if gameboard.board[beta][alpha] == '|':
        return 'pipe'

    if gameboard.board[beta ][alpha ] == 'E':
        return 'enemy'

    if gameboard.board[beta ][alpha ] == 'S':
        return 'spring'

    if gameboard.board[beta][alpha] == 'X':
        return 'wall'

    if gameboard.board[beta ][alpha] == 'H' or gameboard.board[beta][alpha+1] == 'H' :
        return 'tile'

    if gameboard.board[beta][alpha] == ' ':
        return 'empty'

    if gameboard.board[beta ][alpha] == 'B':
        return 'bomberman'

    if gameboard.board[beta ][alpha] == '$':
    	return 'coin'

    if gameboard.board[beta ][alpha ] == 'e':
        return 'explosion'

    return 'lol'

def checkboard2(self,alpha,beta):
	for j in range(0,2):
		for i in range	(1,8):
			if gameboard.board[beta-i][alpha+j] == '$':
				return 'coin'
			if gameboard.board[beta-i][alpha+j] == '@':
				return 'tile'
	return 'empty' 