import Tkinter as tk

class Display(tk.Frame):
	DEFAULT_TITLE = "Game Display"
	HEIGHT = 600
	WIDTH = 600

	CANVAS_FILL = "#000"
	TILE_LIGHT_FILL = "#e8bb97"
	TILE_LIGHT_TEXT_FILL = "#d28a53"
	TILE_DARK_FILL = "#d28a53"
	TILE_DARK_TEXT_FILL = "#ad7144"

	def __init__(self, board, title=DEFAULT_TITLE, master=None):
		self.board = board
		self.tile_width = self.WIDTH / self.board.SIZE
		self.tile_height = self.HEIGHT / self.board.SIZE
		self._initialize_gui(title, master)

	def render(self):
		self._clear_board()
		self._draw_board()
		self.update()

	def _initialize_gui(self, title, master):
		tk.Frame.__init__(self, master)
		self.master.resizable(width=False, height=False)
		self.master.title(title)
		self.grid()

		self.canvas = tk.Canvas(self, height=self.HEIGHT, width=self.WIDTH,
			bg=self.CANVAS_FILL, bd=0, highlightthickness=0)
		self.canvas.grid()

		self._draw_background()

	def _draw_background(self):
		for i in range(self.board.SIZE):
			for j in range(self.board.SIZE):
				x0 = i * self.tile_width
				y0 = j * self.tile_height
				x1 = (i + 1) * self.tile_width
				y1 = (j + 1) * self.tile_height
				label = str(i + (j * self.board.SIZE))

				if (i + j) % 2 == 0:
					fill = self.TILE_LIGHT_FILL
					text_fill = self.TILE_LIGHT_TEXT_FILL
				else:
					fill = self.TILE_DARK_FILL
					text_fill = self.TILE_DARK_TEXT_FILL
				
				self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill, width=0)
				self.canvas.create_text(x0 + 10, y0 + 10, text=label, fill=text_fill)

	def _draw_board(self):
		self.images = []
		for i in range(self.board.SIZE):
			for j in range(self.board.SIZE):
				piece = self.board.pieces[i + (j * self.board.SIZE)]
				if piece:
					image = tk.PhotoImage(file=piece.image)
					# save reference to image or Tkinter won't display it
					self.images.append(image)
					x = (i * self.tile_width) + self.tile_width / 2
					y = (j * self.tile_height) + self.tile_height / 2
					id = self.canvas.create_image(x, y, image=image, tag="piece")

	def _clear_board(self):
		self.canvas.delete("piece")