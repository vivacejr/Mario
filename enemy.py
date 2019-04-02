from board import gameboard
from check import checkboard
from manage import gameManager
class Enemy():
    # The Coordinates of enemy pushed here.
   
    #encapsulation
    _walkingspeed = -1
    
    def __init__(self):
        self.aEnemy = []
        self.vEnemy = []
        self.mark = []
        self.Enemies = 5

        self.aEnemy.append(118)
        self.aEnemy.append(198)
        self.aEnemy.append(218)
        self.aEnemy.append(278)
        self.aEnemy.append(288)

        for i in range (0,self.Enemies):
            self.vEnemy.append(Enemy._walkingspeed)
            self.mark.append(0)
 
    def moveenemies(self):
    	for i in range(0,self.Enemies):
            if self.mark[i] == 0:
                if self.aEnemy[i]<gameboard.st+80:
                    if checkboard(self,self.aEnemy[i] + self.vEnemy[i],28) == 'empty' and self.aEnemy[i] + self.vEnemy[i] < gameboard.st+80 :
                        gameboard.board[28][self.aEnemy[i]]=' ' 
                        self.aEnemy[i] = self.aEnemy[i] + self.vEnemy[i]
                    elif checkboard(self,self.aEnemy[i] + self.vEnemy[i],28) == 'mario':
                        gameManager.changelives()
                        gameboard.board[28][self.aEnemy[i]]=' ' 
                        self.aEnemy[i] = self.aEnemy[i] + -5*self.vEnemy[i] 
                    else:
                        self.vEnemy[i] = self.vEnemy[i]*(-1)

    def printenemies(self):
    	for i in range(0,self.Enemies):
            if self.mark[i] == 0:
                if self.aEnemy[i]<gameboard.st+80 :
                    gameboard.board[28][self.aEnemy[i]]= 'E'

    def killenemy(self,pos):
        for i in range(0,self.Enemies):
            if self.aEnemy[i] == pos:
                self.mark[i] = 1

dushman = Enemy()