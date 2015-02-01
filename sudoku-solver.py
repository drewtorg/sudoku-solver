def main():
	f = open('input.txt')

	#make a list out of the file
	lst = list(f)

	#convert the string list to a 2d list of integers
	sudokuList = [[],[],[],[],[],[],[],[],[]]
	
	i = 0
	for line in lst:
		for char in line:
			if char >='1' and char <= '9':
				sudokuList[i].append(int(char))
		i+=1

	#output for debugging purposes
	#for row in sudokuList:
	#	output = ''
	#	for num in row:
	#		output += str(num) + ' '
	#	print output + '\n'
	
	f.close()

	solve(sudokuList)

def solve(board):
	i = j = nextInt = 0
	while i < len(board):
		while j < len(board[i]):
			#add the nextInt to the board and check validity
			if board[i][j] == 0:
				if isValidMove(board, i, j, nextInt):
					board[i][j] = nextInt
					nextInt += 1
					j += 1
				else:
					nextInt += 1
			#skip this spot in the list
			else:
				j += 1

def checkBox(board, rowIndex, colIndex, nextInt):
	return True

def checkRow(board, rowIndex, nextInt):
	for i in board[rowIndex]:
		if i == nextInt:
			return False
	return True

def checkColumn(board, colIndex, nextInt):
	for i in len(board):
		if board[i][colIndex] == nextInt:
			return False
	return True

def isValidMove(board, row, col, nextInt):
	if checkRow(board, row, nextInt) and checkColumn(board, col, nextInt) and checkBox(board, row, col, nextInt):
		return True
	return False