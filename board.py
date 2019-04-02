from colorama import init, Fore, Back, Style


class Board:
    def __init__(self):
        self.board = [[] for i in range(0, 32)]
        for i in range(0, 32):
            for j in range(0,4000):
                self.board[i].append(' ')

        for j in range (0,8):
            if j%2==0:
                self.board[23][40 + j] = '@'
                self.board[23][100 + j] = '@'
                self.board[23][200 + j] = '@'

        self.board[23][42]='$'
        self.board[23][102]='$'
        self.board[23][200]='$'

        for i in range (25,30):
            for j in range (0,4):
                if i == 25:
                    self.board[i][120+j]= 'T'
                    self.board[i][180+j]= 'T'
                    self.board[i][220+j]= 'T'
                else:
                    self.board[i][120+j]= 'I'
                    self.board[i][180+j]= 'I'
                    self.board[i][220+j]= 'I'



        for i in range (27,29):
            for j in range (0,2):
                if i == 27:
                    self.board[i][240+j]='S'
                    self.board[i][289+j]='S'
                    
                else:
                    self.board[i][240+j]='P'
                    self.board[i][289+j]='P'

        for i in range (18,30):
            for j in range (0,4):
                if i == 18:
                    self.board[i][244+j]= 'T'
                else:
                    self.board[i][244+j]= 'I'

        for j in range (0,8):
            if j%2==0:
                self.board[12][249 + j] = '@'

        for j in range (0,23):
            # if j % 4 ==3:
            self.board[12][256+j]='~'

        for j in range (0,8):
            if j%2==0:
                self.board[12][279 + j] = '@'
        
        self.st=0
   

    def getprint(self):
        if self.st >= 350:
            quit()
        x=self.st
        y=self.st+80
        for i in range(0, 32):
            temp = ''
            for j in range(self.st,self.st+80):
                if i < 2 or j < self.st + 2 or ( i >= 29 and j!=155 and j!=156 and j!=157):
                    self.board[i][j] = "X"
                temp = temp + self.board[i][j]
            for i in range(0,80):
                if temp[i] == 'E' or temp[i]=='<' or temp[i]=='>' :
                    print (Fore.RED + temp[i],end="")
                    print (Style.RESET_ALL,end="")
                elif temp[i] == 'I':
                    print (Fore.GREEN + temp[i],end="")
                    print (Style.RESET_ALL,end="")
                elif temp[i] == 'O' or temp[i]=='T':
                    print (Fore.CYAN + temp[i],end="")
                    print (Style.RESET_ALL,end="")
                elif temp[i] == '@':
                    print (Fore.RED + temp[i],end="")
                    print (Style.RESET_ALL,end="")   
                elif temp[i] == 'X' or temp[i] == 'B' or temp[i]=='|':
                    print (Fore.YELLOW + temp[i],end="")
                    print (Style.RESET_ALL,end="")
                elif temp[i] == '$':
                    print (Fore.MAGENTA  + temp[i],end="")
                    print (Style.RESET_ALL,end="")
                elif temp[i] == '~':
                    print (Fore.GREEN + temp[i],end="")
                    print (Style.RESET_ALL,end="")
                elif temp[i] == 'S' or temp[i] == 'P':
                    print (Fore.BLUE + temp[i],end="")
                    print (Style.RESET_ALL,end="")
                
                else:
                    print (temp[i],end="") 

            print ()

gameboard = Board()