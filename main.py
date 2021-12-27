from game import Game

print('AI player?(X|O|N)')
ai_player = input()

if ai_player not in ['X', 'O']:
	ai_player = None

game = Game(ai_player)

game.run()
