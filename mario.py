import signal
from board import gameboard
from enemy import dushman
from manage import gameManager
from check import checkboard
from check import checkboard2
from boss import thanos
from boss import Boss
from alarmexception import AlarmException
from getch import _getChUnix as getChar
import time

class Mario(Boss):

    #inheritance
    def __init__(self,f,l):
        Boss.__init__(self,f,l)
        self.mark = 0 
        self.inAir=0
        self.superjump=16
        self.superpower=0;
        self.jump = 8
        # self.s = sound()
        # s.read('s1.mp3')

    def generatemario(self):
        for j in range(0, 2):
            gameboard.board[self.y-1][self.x + j] = "O"
            gameboard.board[self.y][self.x + j] = "T"

    #polymorphism
    def move(self):

        def alarmhandler(signum, frame):
            raise AlarmException

        def user_input(timeout=0.1):
            ''' input method '''
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                text = getChar()()
                signal.alarm(0)
                return text
            except AlarmException:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''


        # if Mario.flag == 0: 
        char = user_input()

        if char == 'i':
            gameManager.lives += 1

        # Press 'q' for quit.
        if char == 'q':
        	quit()

        # Press 'w' for up.


        if char == 'w' and checkboard2(self, self.x  ,self.y  ) == 'empty' and (checkboard(self, self.x  ,self.y +1  ) != 'empty' or checkboard(self, self.x +1  ,self.y + 1 ) != 'empty'):
            if (self.x==285 or self.x == 284) and self.y==11:
                self.superpower=1;
                gameboard.board[8][283]='S'
                gameboard.board[8][284]='P'
            for i in range(0,4):
                for j in range(0, 2):
                    gameboard.board[(self.y - 1)-2*i][self.x + j] = ' '
                    gameboard.board[self.y - 2*i][self.x + j ] = ' '
            self.y = self.y - self.jump

        if char == 'w' and checkboard2(self, self.x,self.y ) == 'tile' :
            for i in range(0,1):
                for j in range(0,2):
                    gameboard.board[(self.y - 1)-2*i][self.x + j] = ' '
                    gameboard.board[self.y - 2*i][self.x + j ] = ' '
            self.y = self.y - 3

        if char == 'w' and checkboard2(self, self.x,self.y ) == 'coin' :
            for i in range(0,4):
                for j in range(0,2):
                    gameboard.board[(self.y - 1)-2*i][self.x + j] = ' '
                    gameboard.board[self.y - 2*i][self.x + j ] = ' '
            gameManager.changescore('coin') 
            self.y = self.y - 6


        if char == 'a' and checkboard(self, self.x - 1 ,self.y ) == 'empty' and checkboard(self, self.x - 1 ,self.y -1 ) == 'empty':
            for j in range(0, 2):
                gameboard.board[(self.y - 1)][self.x + j] = ' '
                gameboard.board[self.y][self.x + j ] = ' '
            self.x = self.x - 1


        if char == 'd' and checkboard(self, self.x + 2   ,self.y ) == 'empty' and checkboard(self, self.x + 2  ,self.y -1  ) == 'empty':
            if self.x == gameboard.st + 40:
                gameboard.st = gameboard.st + 1
                # Mario.a = gameboard.st + 40
            for j in range(0, 2):
                gameboard.board[(self.y - 1)][self.x + j] = ' '
                gameboard.board[self.y][self.x + j ] = ' '

            self.x = self.x + 1

        #pit
        if self.y >29:
            for j in range(0, 2):
                gameboard.board[(self.y - 1)][self.x + j] = ' '
                gameboard.board[self.y][self.x + j ] = ' '
            gameManager.changelives()
            self.x = self.x-3;
            self.y = 28

        if  checkboard(self, self.x  ,self.y + 1 ) == 'empty' and checkboard(self, self.x + 1  ,self.y + 1 ) == 'empty' :
            for j in range(0, 2):
                gameboard.board[(self.y - 1)][self.x + j] = ' '
                gameboard.board[self.y][self.x + j ] = ' '
            self.y = self.y + 1

        if  checkboard(self, self.x  ,self.y + 1 ) == 'spring' or checkboard(self, self.x + 1  ,self.y + 1 ) == 'spring' :
            for j in range(0, 2):
                gameboard.board[(self.y - 1)][self.x + j] = ' '
                gameboard.board[self.y][self.x + j ] = ' '
            self.y = self.y - 20

        if  checkboard(self, self.x  ,self.y + 1 ) == 'enemy' or checkboard(self, self.x + 1  ,self.y + 1 ) == 'enemy' :
            # s.play()
            dushman.killenemy(self.x)
            dushman.killenemy(self.x + 1)
            gameManager.changescore('enemy') 
            for j in range(0, 2):
                gameboard.board[(self.y - 1)][self.x + j] = ' '
                gameboard.board[self.y][self.x + j ] = ' '
            self.y = self.y + 1
        
        if  checkboard(self, self.x  ,self.y + 1 ) == 'boss' or checkboard(self, self.x + 1  ,self.y + 1 ) == 'boss' :
            gameManager.changescore('boss') 
            thanos.killboss()
            for j in range(0, 2):
                gameboard.board[(self.y - 1)][self.x + j] = ' '
                gameboard.board[self.y][self.x + j ] = ' '
            self.y = self.y + 1    

        if self.superpower == 1:
            self.jump = self.superjump    
        for j in range(0, 2):
                    gameboard.board[(self.y - 1)][self.x + j] = 'O'
                    gameboard.board[self.y][self.x + j ] = 'T'


