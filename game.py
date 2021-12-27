class Game:
	def __init__(self, ai_player = None):
		self.board = [[' ' for _ in range(3)] for _ in range(3)]
		self.ai_player = ai_player
	
	def move(self, action):
		if self.board[action[0]][action[1]] != ' ':
			raise 'Invalid move'
		
		self.board[action[0]][action[1]] = self.player
	
	def switch_player(self):
		if self.player == 'X':
			self.player = 'O'
		else:
			self.player = 'X'
	
	def ai_action(self, depth = 0, is_maximizer=True):
		best_score = None
		best_action = None
		for i in range(3):
			for j in range(3):
				if self.board[i][j] != ' ':
					continue
				action = (i, j)
				self.move(action)
				score = self.score_map(self.check_winner())
				
				if score is None:
					self.switch_player()
					_, score = self.ai_action(depth + 1, not is_maximizer)
					self.switch_player()
				
				if is_maximizer:
					if best_score is None or score > best_score:
						best_score = score
						best_action = action
				else:
					if best_score is None or score < best_score:
						best_score = score
						best_action = action
				self.board[i][j] = ' '
				
		return best_action, best_score
		
				
	def score_map(self, result):
		if result == self.ai_player:
			return 1
		elif result == 'tie':
			return 0
		elif result is None:
			return result
		return -1
		
	def check_winner(self):
		winner = None
		
		for i in range(3):
			if self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2] and self.board[i][0] != ' ':
				winner = self.board[i][0]
				break;
			if self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i] and self.board[0][i] != ' ':
				winner = self.board[0][i]
				break
		
		if winner is None:
			if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] and self.board[0][0] != ' ':
				winner = self.board[1][1]
			elif self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0] and self.board[0][2] != ' ':
				winner = self.board[1][1]

		if winner is not None:
			return winner
		
		is_full = True
		
		for i in range(3):
			for j in range(3):
				if self.board[i][j] == ' ':
					is_full =  False
					break
		
		if is_full:
			return 'tie'
		
		return None
	
	def __str__(self):
		result = ''
		result += '_______\n'
		for i in range(3):
			result += '|' + self.board[i][0] + '|' + \
				self.board[i][1] + '|' + self.board[i][2] + '|\n'
			result += '_______\n'
		return result
	
	def run(self):
		self.player = 'X'
		while self.check_winner() is None:
			print(self)
			if self.player == self.ai_player:
				action, _ = self.ai_action()
				self.move(action)
				print('AI player', self.player, 'moved!')
			else:
				print('Player', self.player, 'move:')
				action = input().split()
				action = [int(e) for e in action]
				self.move(action)
			self.switch_player()
		
		print(self)
		print('Result:', self.check_winner())
