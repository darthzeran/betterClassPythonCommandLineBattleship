
# Constants
SQUARE_TYPE = {'NONE': ' ', 'HIT': 'X', 'MISS': 'O'}
MAX_ROWS = 10
MAX_COLUMNS = 10


# BOARD STYLING
letters = "ABCDEFGHIJ"
boxPadding = "|      "
rowPadding = (boxPadding * 10) + "|\n"
boxBorder = "  |" + ("-" * 69) + "|\n"


class BattleshipBoard:
	def __init__(self, id):
		self.id = id
		self.board = [[{'ship': None, 'type': SQUARE_TYPE['NONE']} for _ in range(MAX_COLUMNS)] for _ in range(MAX_ROWS)]

		
	def preset(self):
		self.addShip("A1", "A5", 5)
		self.addShip("B1", "B4", 4)
		self.addShip("C1", "C3", 3)
		self.addShip("D1", "D3", 3)
		self.addShip("E1", "E2", 2)
		
		self.printBoard(True)
	
	
	def placeShips(self):
		return self.preset()
		
		self.setupShip( "aircraft carrier", 5)
		self.setupShip( "battleship", 4)
		self.setupShip( "destroyer", 3)
		self.setupShip( "submarine", 3)
		self.setupShip( "cruiser", 2)
		
	def setupShip(self, ship_name, size):
		self.printBoard(True)
		start = None
		end = None
		
		while (not self.validateShipPlacement(start, end, size)) or (not self.isFreeOfShips(start, end, size)):
			start = input("Player " + str(self.id) + ", Where would you like your " + ship_name + " (size " + str(size) + ") to start? e.g. A1: ")
			end = input("Player " + str(self.id) + ", Where would you like your " + ship_name + " (size " + str(size) + ") to end? e.g. A2: ")

		self.addShip(start, end, size)
		print(ship_name + " added!")


	def validateShipPlacement(self, start, end, size):
		if not start or not end:
			return False
		if start == "quit" or end == "quit":
			raise Exception("cheat code to restart")

		try:
			startLetter = start[0].upper()
			endLetter = end[0].upper()
			startNumber = int(start[1:])
			endNumber = int(end[1:])
		except Exception as e:
			print("Issue with your input")
			return False

		return (
			(startLetter == endLetter and abs(startNumber - endNumber) == size - 1)
			or (
				startNumber == endNumber
				and abs(letters.index(startLetter) - letters.index(endLetter)) == size - 1
			)
		)


	def isFreeOfShips(self, start, end, size):
		if not start or not end:
			return False
		try:
			if start[0].upper() == end[0].upper():
				i = int(start[1:]) - 1
				j = letters.index(start[0].upper())
				for k in range(size):
					if self.board[i + k][j]["ship"] != None:
						return False
			else:
				i = int(start[1:]) - 1
				j = letters.index(start[0].upper())
				for k in range(size):
					if self.board[i][j + k]["ship"] != None:
						return False
			return True
		except Exception as e:
			print("Issue with your input, try placing the ships top-down, left-right")
			return False


	def addShip(self, start, end, size):
		if start[0].upper() == end[0].upper():
			i = int(start[1:]) - 1
			j = letters.index(start[0].upper())
			for k in range(size):
				self.board[i + k][j]["ship"] = size
		else:
			i = int(start[1:]) - 1
			j = letters.index(start[0].upper())
			for k in range(size):
				self.board[i][j + k]["ship"] = size


	def evaluateGuess(self, guess):
		if not guess:
			print("Wasted turn")
			return False
		try:
			row = int(guess[1:]) - 1
			col = letters.index(guess[0].upper())
			if col < 0 or col > 9 or row < 0 or row > 9:
				print("Wasted turn")
				return False

			spot = self.board[row][col]

			if spot["type"] != SQUARE_TYPE["NONE"]:
				print("Wasted turn")
				return False

			if spot["ship"]:
				print("HIT")
				spot["type"] = SQUARE_TYPE["HIT"]
				return True
			else:
				print("MISS")
				spot["type"] = SQUARE_TYPE["MISS"]
				return False
		
		except Exception as e:
			print("Wasted turn")
			return False


	def isBoardSolved(self):
		for i in range(MAX_ROWS):
			for j in range(MAX_COLUMNS):
				spot = self.board[i][j]
				if spot["ship"] and spot["type"] != SQUARE_TYPE["HIT"]:
					return False
		return True


	def printBoard(self, showShips):
		header = "      A      B      C      D      E      F      G      H      I      J   \n"
		boardOutput = "\n" + header
		boardOutput += boxBorder

		for row in range(MAX_ROWS):
			boardOutput += "  " + rowPadding
			if row + 1 > 9:
				boardOutput += str(row + 1) + ""
			else:
				boardOutput += str(row + 1) + " "

			for column in range(MAX_COLUMNS):
				spot = self.board[row][column]
				boxChar = ""
				if showShips and spot["ship"]:
					boxChar = spot["ship"]
				else:
					boxChar = spot["type"]
				boardOutput += "|   " + str(boxChar) + "  "

			boardOutput += "| " + str(row + 1) + "\n"
			boardOutput += "  " + rowPadding
			boardOutput += boxBorder

		boardOutput = boardOutput + header
		print(boardOutput)
	
