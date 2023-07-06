
from BattleshipBoard import BattleshipBoard

class Game:
	def __init__(self):		
		self.state = self.getNewState()

	def getNewState(self):
		return {
			"visible_board": True,
			"player_1_turn": True,
			"player_1_board": BattleshipBoard(1),
			"player_2_board": BattleshipBoard(2),
		}
	
	def setup(self):
		self.state['player_1_board'].placeShips()
		self.state['player_2_board'].placeShips()

	
	def start(self):
		while True:
			# get turn constants
			cur_player_id = str(1 if self.state["player_1_turn"] else 2)
			dormant_player_id = str(2 if self.state["player_1_turn"] else 1)
			goAgain = False

			# alert the player whose turn it is, and show their opps board
			print("\nPlayer " + cur_player_id + " it is your turn")
			self.printPlayerBoard(dormant_player_id)

			guess = input("Where should we aim? (Enter QUIT to save and quit): ")
			if guess.upper() == "QUIT":
				return "SAVE"
			else:
				# if its a hit, go again
				goAgain = self.state['player_' + dormant_player_id + '_board'].evaluateGuess(guess)


			if self.state['player_' + dormant_player_id + '_board'].isBoardSolved():
				print("\n!Player " + cur_player_id + " wins!\n")
				break
			if not goAgain:
				self.state["player_1_turn"] = not self.state["player_1_turn"]
	
	
	def printPlayerBoard(self, playerId):
		if self.state['visible_board']:
			self.state['player_' + playerId + '_board'].printBoard(False)