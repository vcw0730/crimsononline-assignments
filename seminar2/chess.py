import operator
from game import BoardGame, Board, Piece, Player

class Chess(BoardGame):
	def __init__(self):
		super(Chess, self).__init__()

	def _initialize_board(self):
		self.board = ChessBoard(*self.players)

class ChessBoard(Board):
	SIZE = 8

	def __init__(self, p1, p2):
		self.pieces = (
			[Rook(p1), Knight(p1), Bishop(p1), Queen(p1),
			 King(p1),Bishop(p1), Knight(p1), Rook(p1)] +
			[Pawn(p1) for i in range(8)] +
		    [None] * 32 +
			[Pawn(p2) for i in range(8)] +
			[Rook(p2), Knight(p2), Bishop(p2), Queen(p2),
			 King(p2), Bishop(p2), Knight(p2), Rook(p2)]
		)

	def valid_move(self, move, player):
		def fail(message):
			print message
			return False

		start, end = move
		try:
			start_piece = self.pieces[start]
			end_piece = self.pieces[end]
		except IndexError:
			return fail("Position off the board")

		if not start_piece:
			return fail("There's no piece at {}".format(start))
	 	if start_piece.player != player:
			return fail("That's not your piece")

		start_coords = self._position_to_coords(start)
		end_coords = self._position_to_coords(end)
		path = start_piece.get_path(*(start_coords + end_coords))
		delta = self._coords_delta(start_coords, end_coords, reverse=player.id % 2 == 1)

		if self._valid_path(path):
			if end_piece:
				if end_piece.player == player:
					return fail("You can't capture your own piece")
				else:
					print start_piece.valid_capture(*delta)
					return start_piece.valid_capture(*delta)
			else:
				return start_piece.valid_move(*delta)
		return False

	def move(self, move):
		start, end = move
		self.pieces[end] = self.pieces[start]
		self.pieces[start] = None

	def _valid_path(self, path):
		for coords in path:
			position = self._coords_to_position(coords)
			if self.pieces[position] != None:
				return False
		return True

	def _coords_delta(self, start_coords, end_coords, reverse=False):
		if reverse: start_coords, end_coords = end_coords, start_coords
		return map(operator.sub, end_coords, start_coords)

	def _position_to_coords(self, pos):
		return (pos / self.SIZE, pos % self.SIZE)

	def _coords_to_position(self, coords):
		row, col = coords
		return (row * self.SIZE + col)

class ChessPiece(Piece):
	def get_path(self, row_start, col_start, row_end, col_end):
		row_adj = 1 if row_end > row_start else -1
		col_adj = 1 if col_end > col_start else -1
		row_path = range(row_start + row_adj, row_end, row_adj)
		col_path = range(col_start + col_adj, col_end, col_adj)

		if row_start == row_end:
			row_path = [row_start] * len(col_path)
		if col_start == col_end:
			col_path = [col_start] * len(row_path)

		return zip(row_path, col_path)

class King(ChessPiece):
	def valid_move(self, row_delta, col_delta):
		return abs(row_delta) <= 1 and abs(col_delta) <= 1

class Queen(ChessPiece):
	def valid_move(self, row_delta, col_delta):
		return ((row_delta == 0 or col_delta == 0) or
			abs(row_delta) == abs(col_delta))

class Rook(ChessPiece):
	def valid_move(self, row_delta, col_delta):
		return row_delta == 0 or col_delta == 0

class Bishop(ChessPiece):
	def valid_move(self, row_delta, col_delta):
		return abs(row_delta) == abs(col_delta)

class Knight(Piece):
	def valid_move(self, row_delta, col_delta):
		return (abs(row_delta) == 1 and abs(col_delta) == 2 or
			abs(row_delta) == 2 and abs(col_delta) == 1)

	def get_path(self, row_start, col_start, row_end, col_end):
		return []

class Pawn(ChessPiece):
	def valid_move(self, row_delta, col_delta):
		return row_delta == 1 and col_delta == 0

	def valid_capture(self, row_delta, col_delta):
		return row_delta == 1 and abs(col_delta) == 1

if __name__ == "__main__":
	Chess().start()