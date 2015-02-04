#As a note of interest, I screwed around for a few hours trying to get the right algorithm and for some reason it was just barely off.
#After consulting the internet I found this website http://spin.atomicobject.com/2012/06/18/solving-sudoku-in-c-with-recursive-backtracking/
#which helped me find the kinks in my algorithm and I ended up using his algorithm just because it ended up looking prettier than mine.  All
#credit goes to Mitchell Johnson, thanks for helping me solve this problem.

def solveCell(board, row, col):
	if row == 9:
		return True

	if not board[row][col] == 0:
		if col == 8:
			if solveCell(board, row + 1, 0):
				return True
		else:
			if solveCell(board, row, col + 1):
				return True
		return False

	for nextInt in range(1, 10):
		if isValidMove(board, row, col, nextInt):
			board[row][col] = nextInt
			if col == 8:
				if solveCell(board, row + 1, 0):
					return True
			else:
				if solveCell(board, row, col + 1):
					return True

	board[row][col] = 0

def checkBox(board, rowIndex, colIndex, nextInt):
	sectorRow = 3 * (rowIndex/3)
	sectorCol = 3 * (colIndex/3)
	row1 = (rowIndex + 2) % 3
	row2 = (rowIndex + 4) % 3
	col1 = (colIndex + 2) % 3
	col2 = (colIndex + 4) % 3

	if board[row1 + sectorRow][col1 + sectorCol] == nextInt:
		return False
	if board[row2 + sectorRow][col1 + sectorCol] == nextInt:
		return False
	if board[row1 + sectorRow][col2 + sectorCol] == nextInt:
		return False
	if board[row2 + sectorRow][col2 + sectorCol] == nextInt:
		return False
	return True
	print 'hello'

def checkRowAndColumn(board, rowIndex, columnIndex, nextInt):
	for i in range(9):
		if board[i][columnIndex] == nextInt:
			return False
		if board[rowIndex][i] == nextInt:
			return False
	return True

def isValidMove(board, row, col, nextInt):
	return checkRowAndColumn(board, row, col, nextInt) and checkBox(board, row, col, nextInt)

def convertList(input):
	sudokuList = [[],[],[],[],[],[],[],[],[]]
	
	i = 0
	for line in input:
		for char in line:
			if char >='0' and char <= '9':
				sudokuList[i].append(int(char))
		i+=1
	return sudokuList

def printRow():
	out = ''
	for i in range(22):
		out += '-'
	print out

def printBoard(board):

	rowCount = 0
	colCount = 0
	for i in board:
		if rowCount % 3 == 0:
			printRow()
		out = ''
		for j in i:
			if colCount % 3 == 0:
				out += '|'
			if j == 0:
				out += '  '
			else:
				out += str(j) + ' '
			colCount += 1
		print out + '|'
		rowCount += 1

	printRow()

def main():
	f = open('empty.txt')

	#make a list out of the file
	lst = list(f)

	#convert the string list to a 2d list of integers
	sudokuList = convertList(lst)
	
	f.close()
	print 'Before:'
	printBoard(sudokuList)

	solveCell(sudokuList, 0, 0)

	print 'After:'
	printBoard(sudokuList)

main()