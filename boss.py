from board import gameboard
from manage import gameManager
from manage import Manage
from check import checkboard
import os	
import time
import random
class Boss():

	def __init__(self,f,l):
		self.x= f
		self.y=l
		self.missile = []
		self.missileV = []
		self.missilemark = []
		self.missilecnt = 0
		self.mark=0

	def move(self,a):
		# print (Mario.x)
		if self.mark ==0 :
			for i in range(21,29):
				gameboard.board[i][self.x+1]=' '
			gameboard.board[21][self.x]=' '
			gameboard.board[21][self.x+2]=' '

			if self.x < a + 30 and self.x > a :
				if checkboard(self,self.x-1,28) =='mario' or checkboard(self,self.x-1,27) =='mario' or checkboard(self,self.x-1,26) =='mario' or checkboard(self,self.x-1,25) =='mario' or checkboard(self,self.x-1,24) =='mario'or checkboard(self,self.x-1,23) =='mario':
					self.x =self.x+5
					gameManager.changelives()
				else:
					self.x = self.x-1
			elif self.x > a - 30 and self.x < a :
				if checkboard(self,self.x+1,28) =='mario':
					self.x =self.x-5
					gameManager.changelives()
				else: 	
					self.x = self.x +1

	def printboss(self):
		if self.mark ==0:
			gameboard.board[21][self.x]='\\'
			gameboard.board[21][self.x+1]='_'
			gameboard.board[21][self.x+2]='/'
			gameboard.board[22][self.x+1]='B'
			gameboard.board[23][self.x+1]='|'
			gameboard.board[24][self.x+1]='O'
			gameboard.board[25][self.x+1]='|'
			gameboard.board[26][self.x+1]='S'
			gameboard.board[27][self.x+1]='|'
			gameboard.board[28][self.x+1]='S'

	def bossattack(self,a):
		if self.mark==0:	
			k = random.uniform(0,5)
			if k <= 0.3:
				if self.x < a + 30 and self.x > a :
					self.missile.append(self.x-1)
					self.missileV.append(-1)
					self.missilemark.append(0)
					self.missilecnt = self.missilecnt +1
				elif self.x > a - 30 and self.x < a : 
					self.missile.append(self.x+1)
					self.missileV.append(1)
					self.missilemark.append(0)
					self.missilecnt = self.missilecnt +1


	def movebullets(self,a):
		if self.mark == 0:
			for i in range (0,self.missilecnt):
				if self.missilemark[i] == 0:	
					gameboard.board[27][self.missile[i]]=' '
					if checkboard(self,self.missile[i]+self.missileV[i],27) == 'empty' :
						self.missile[i]=self.missile[i] + self.missileV[i]
					elif self.missile[i]+self.missileV[i] == a or self.missile[i]+self.missileV[i] == a+1:
						gameManager.changelives()
						self.missilemark[i] = 1
					else:
						self.missilemark[i] = 1


	def printbullets(self):
		if self.mark == 0:
			for i in range (0,self.missilecnt):
				if self.missilemark[i] == 0:	
					if self.missileV[i] == -1:
						gameboard.board[27][self.missile[i]] = '<'
					else:
						gameboard.board[27][self.missile[i]] = '>'

	def killboss(self):
		self.mark = 1
		for i in range(21,29):
			gameboard.board[i][self.x+1]=' '
			gameboard.board[21][self.x]=' '
			gameboard.board[21][self.x+2]=' '
		os.system("tput reset")
		print ("YOU WIN")
		time.sleep(2)
		exit()
thanos = Boss(350,28)