from Game import Game
import copy


class Battleship:
	def __init__(self):
		self.saved_games = {}
		self.currentGame = Game()

	def on(self):
		option = 0
		while(option != '5'):
			self.showMenu()
			option = input("Enter menu option: ")
			try:
				self.selectChoice(option)
			except Exception as e:
				print('Restarting game loop :)')
			
		print("GG\n\n")
			

	def showMenu(self):
		print("\nWelcome to BattleShip! (NOT the movie)\n")
		print("Please select an option:")
		print("1 Start new game")
		print("2 Load saved game")
		print("3 See rules")
		print("4 Settings")
		print("5 Quit\n")
	
	def runGame(self):
			msg = self.currentGame.start()
			if msg == "SAVE":
				gameName = input(
					"Enter a name to save this game under, it will overwrite anything with the same name: "
				)
				self.saved_games[gameName] = copy.deepcopy(self.currentGame)
				print("See you soon!\n")
				
			# game is over, reset board
			self.currentGame = Game()

	def selectChoice(self, c):
		if c == '1':
			self.currentGame.setup()
			self.runGame()

		elif c == '2':
			game_found = self.loadSavedGame()
			if game_found:
				self.runGame()
				
		elif c == '3':
			print("\n\nYou don't know how to play BattleShip?... FFFF\n")
		elif c == '4':
			print("Sorry we only have 1 setting")
			print("Enter Yes/yes/Y/or y if you want to play with a visible board.")
			print("Any other option will make the board invisible\n")
			choice = input("Show board?: ")
			if choice.upper() in ["YES", "Y"]:
				self.currentGame.state["visible_board"] = True
			else:
				self.currentGame.state["visible_board"] = False
		elif c == '5':
			return
		else:
			print("Input Error, try again\n\n")
			
		
	def loadSavedGame(self):
		msg = "Choose a game by its game name:\n"
		for gameName in self.saved_games.keys():
			msg += "- " + gameName + "\n"
		msg += "\nYour choice-> "

		chosenGameName = input(msg)
		if chosenGameName in self.saved_games:
			self.currentGame = copy.deepcopy(self.saved_games[chosenGameName])
			return True
		else:
			print("Game not found :(\n\n")
			return False
	

if __name__ == '__main__':
	game = Battleship()
	game.on()
