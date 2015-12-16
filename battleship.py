# Battle Ship Game !
from random import randint

board = []

for i in range(5):
	board.append(["O"] * 5)


def showBoard():
	print "------------"
	for i in board:
		print " ".join(i)
	print "------------"


ship_r = randint(0,4)
ship_c = randint(0,4)

print "*** Enter number 0 - 4 ***"
print "Enemy Ship on the Board[%s][%s]" % (ship_r ,ship_c)

for i in range(4):	
	showBoard()
	print "Turn " + str(i+1)
	
	guess_r = int(raw_input("Enter row : "))
	guess_c = int(raw_input("Enter colonm : "))

	if ship_r == guess_r and ship_c == guess_c :
		board[guess_r][guess_c] = "!"
		print "Oparetor: Boom!"
		showBoard()
		break
	elif ( guess_r < 0 or guess_r > 4 ) or ( guess_c < 0 or guess_c > 4 ) :
		showBoard()
		print "Oparetor: Over the area. Byee ~"
	elif board[guess_r][guess_c] == "X" :
		showBoard()
		print "Oparetor: Can't Attack."
	else:
		board[guess_r][guess_c] = "X"
		showBoard()
		print "Oparetor: Miss ~"

print "Oparetor: enemy Ship on the Board[%s][%s]" % (ship_r ,ship_c)
