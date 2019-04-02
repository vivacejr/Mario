import os
from mario import Mario
from manage import gameManager
from enemy import dushman
from boss import thanos
from board import gameboard
from clouds import Cloud
TEST = Mario(4,28)
TEST1 = dushman
TEST2 = thanos	
TEST3 = gameboard
TEST4 = gameManager
print("")
print("Mario")
print("")
print("Press Enter to start")

Start = input()

TEST3.getprint()
TEST.generatemario()

scene = []


#creating cloud objects
c1 = Cloud(10,8)
c2 = Cloud(30,10)
c3 = Cloud(50,8)
c4 = Cloud(70,8)
c5 = Cloud(100,8)
c6 = Cloud(130,10)
c7 = Cloud(170,10)
c8 = Cloud(200,8)
scene.append(c1)
scene.append(c2)
scene.append(c3)
scene.append(c4)
scene.append(c5)
scene.append(c6)
scene.append(c7)
scene.append(c8)



	
# TEST.__init__()
# TEST.generatetiles()
# TEST.generateenemies()

i=0
j=0
while 1:
	os.system("tput reset")
	TEST4.printhead()
	# TEST.cleargameboard()
	for k in scene:
		k.printcloud()
	TEST3.getprint()
	TEST1.moveenemies()
	TEST1.printenemies()
	if i == 3:
		TEST2.move(TEST.x)
		TEST2.printboss()
		i =0
	TEST2.bossattack(TEST.x)
	TEST2.movebullets(TEST.x)
	TEST2.printbullets()
	TEST.move()
	i = i + 1
