import random
#create dict to convert user input to board list index
userinp={'T1':0,'T2':1,'T3':2,'M1':3,'M2':4,'M3':5,'B1':6,'B2':7,'B3':8}
board=[' ']*9#create board itself
def display(board):
	for i in [0,3,6]:
		if i==0:
			print('_____________')
		print('|',board[i],'|',board[i+1],'|',board[i+2],'|')
		print('_____________')
	print("\n")
def empty():#Check if board is filled
	for i in board:
		if i==' ':
			return True
def winner(board,checktype):
	win=0
	for i in [0,3,6]:
		if board[i]==board[i+1]==board[i+2]!=' ':
			win=board[i]
			break
	for i in [0,1,2]:
		if board[i]==board[i+3]==board[i+6]!=' ':
			win=board[i]
			break
	if board[0]==board[4]==board[8]!=' ' or board[2]==board[4]==board[6]!=' ':
		win=board[4]
	if win!=0 and checktype=='compute':
		return True
	if checktype=='justcheck' and win==0:
		if not empty():
			print("Neither wins")
			display(board)
		return True
	if checktype=='justcheck' and win!=0:
		print(win+" wins!")
		display(board)
def computeplay(mode,computer,player):
	if mode=='simple':
		return random.randint(0,8)
	for pos in range(0,9):#Check Immediate win for computer
		if board[pos]==' ':
			boardx=board[:]
			boardx[pos]=computer#Create possible future board that this move would make
			if winner(boardx,'compute'):
				return pos
	for pos in range(0,9):#Check if enemy may win:
		if board[pos]==' ':
			boardx=board[:]
			boardx[pos]=player
			if winner(boardx,'compute'):
				return pos
	#If no immediate win on either side move based on priority of position
	if board[4]==' ':
		return 4#Max priority since there are 4 ways to win from here
	for pos in [2,8,0,6,1,7,5,3]:#Randomized for mortals to not find patterns
		if board[pos]==' ':
			return pos
#Actual Game:
player=input("What do you want to play as?(X/O): ").upper()
if player=='X':
	computer='O'
else:
	computer='X'
mode=input("What difficulty level do you want?(simple/hard): ")
playfirst=input("Do you want to play first?(y/n): ")
playernow=computer #By default computer plays first
if playfirst=='y':
	playernow=player
while winner(board,'justcheck') and empty():
	display(board)
	if playernow==player:
		pos=userinp[input("Enter position in board as (Row:T,M or B;column:1,2 or 3):  ").upper()]
	else:
		pos=computeplay(mode,computer,player)
	if board[pos]!=' ':#Check if user is trying to place in already filled spot
		print('that position has already been filled!')
		continue
	board[pos]=playernow
	if playernow==player:
		playernow=computer
	else:
		playernow=player
