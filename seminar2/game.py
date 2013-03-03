import os
import sys
from itertools import cycle
from gui import Display

class BoardGame(object):
	def __init__(self):
		self.players = (Player(0), Player(1))
		self._initialize_board()

		self.display = Display(self.board)
		self.display.render()

	def _initialize_board(self):
		self.board = Board(*self.players)

	def start(self):
		players = cycle(self.players)
		while True:
			try:
				player = players.next()
				print "PLAYER {}".format(player.id)
				while True:
					move = player.request_move()
					if self.board.valid_move(move, player):
						break
					print "Invalid move. Try again!"
				self.board.move(move)
				self.display.render()
				print
				print "PIECES REMAINING {}".format(self.board.get_stats())
				print
			except (KeyboardInterrupt, EOFError):
				print
				sys.exit()

class Board(object):
	SIZE = 1

	def __init__(self, p1, p2):
		self.pieces = [None] * self.SIZE * self.SIZE

	def get_stats(self):
		stats = [0, 0]
		for piece in self.pieces:
			if piece:
				stats[piece.player.id] += 1
		return tuple(stats)

	def valid_move(self, move, player):
		raise NotImplementedError

	def move(self, move):
		raise NotImplementedError

class Piece(object):
	IMAGE_ROOT = "images"

	def __init__(self, player):
		self.player = player

	@property
	def image(self):
		filename = "{}_{}.gif".format(self.__class__.__name__.lower(),
			self.player.id)
		return os.path.join(self.IMAGE_ROOT, filename)

	def get_path(self, x, y):
		raise NotImplementedError

	def valid_move(self, x, y):
		raise NotImplementedError

	def valid_capture(self, x_delta, y_delta):
		return self.valid_move(x_delta, y_delta)

class Player(object):
	def __init__(self, id):
		self.id = id

	def request_move(self):
		start = self._request_int("Which piece? ")
		end = self._request_int("Where to? ")
		return (start, end)

	def _request_int(self, prompt):
		while True:
			try:
				return int(raw_input(prompt))
			except ValueError:
				print "Please enter a valid integer"
			except KeyboardInterrupt:
				pass