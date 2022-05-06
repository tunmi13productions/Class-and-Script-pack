"""
Gameboard
tunmi13
This is a simple game board consisting of columns, rows, and pieces.
The code provided here could have possibly been done in other ways. I am not a very good coder, so there are likely better ways of coding this. As such, do not expect any major stuff.
"""
class board:
	"""
	There are two classes that make up this main class.
	The first one is BoardColumn. This is the most important class. BoardColumn contains the rows of the board. This means that it represents the horrizontal and vertical squares of the board.
	BoardRow is a class for BoardColumn. These handles are inserted into BoardColumn, which can then be manipulated, either from the BoardColumn class or from this main class.
	The main class only uses BoardColumn as its handles list, because BoardColumn already does its job by taking care of how many rows  the board has. The columns and rows are then able to be manipulated in this class.
	"""

	def __init__(self,columns=10,rows=10):
		"""Initializes the class.
			Parameters:
				columns (int): The number of columns (or horrizontal squares) that the board should have.
				rows (int): The number of rows (or vertical squares) that the board should have. These will be inserted into each column.
		"""
		self.columns = []
		#Loop through the number of coluns provided.
		for i in range(columns):
			#Create a column with the number of rows specified, then insert the handle into the columns list.
			temp = BoardColumn(rows)
			self.columns.append(temp)

	def whipe(self):
		#Clears the entire board by whiping all its columns, which will also take care of the rows. This is because the columns class uses rows already.
		for i in range(self.columns):
			self.columns[i].whipe()

	def take_piece(self,column,row):
		"""Takes a piece from the specified position on the board. Returns true if the piece was able to be taken, or false on error.
			Parameters:
				column (int): The column you would like to take the piece from. You can also consider this the x axis, if that is easier for you to understand.
				row (int): The row you would like to take the piece from. You can also consider this the y axis, if that is easier for you to understand.
		"""
		if column > len(self.columns)-1 or column < 0: return False
		if row > len(self.columns[column].rows)-1 or row < 0: return False
		if self.columns[column].rows[row].pieces == 0: return False
		self.columns[column].rows[row].pieces -= 1
		return True
	def add_piece(self,column,row):
		"""Adds or drops a piece to the specified position on the board. Returns true if the piece was able to be added, or false on error.
			Parameters:
				column (int): The column you would like to drop the piece on. You can also consider this the x axis, if that is easier for you to understand.
				row (int): The row you would like to drop the piece on. You can also consider this the y axis, if that is easier for you to understand.
		"""

		if column > len(self.columns)-1 or column < 0: return False
		if row > len(self.columns[column].rows)-1 or row < 0: return False
		self.columns[column].rows[row].pieces += 1
		return True
	def take_all_pieces(self,column,row):
		"""Takes all pieces from the specified position on the board. Returns true if the pieces were able to be taken, or false on error.
			Parameters:
				column (int): The column you would like to take the pieces from. You can also consider this the x axis, if that is easier for you to understand.
				row (int): The row you would like to take the pieces from. You can also consider this the y axis, if that is easier for you to understand.
		"""
		if column > len(self.columns)-1 or column < 0: return False
		if row > len(self.columns[column].rows)-1 or row < 0: return False
		if self.columns[column].rows[row].pieces == 0: return False
		self.columns[column].rows[row].pieces -= self.columns[column].rows[row].pieces
		return True
	def get_pieces(self,column,row):
		"""Retrieves information about the amount of pieces from the specified position on the board. Returns the number of pieces if the amount is greater than 0, or 0 if none were found.
			Parameters:
				column (int): You can consider this the x axis, if that is easier for you to understand.
				row (int): You can consider this the y axis, if that is easier for you to understand.
		"""

		if column > len(self.columns)-1 or column < 0: return 0
		if row > len(self.columns[column].rows)-1 or row < 0: return 0
		return self.columns[column].rows[row].pieces


class BoardColumn:
	"""
	This is the BoardColun class, controlled by the main class or can be controlled on its own.
	BoardRow is used in this class. This is because each column has a set of rows. Think of it as a table.
	"""
	def __init__(self,rows,pieces=5):
		"""Initiates the class.
			Parameters:
				rows (int): The number of rows the column should have.
				pieces (int): The number of pieces the rows should have.
		"""
		self.rows = []
		#Loop through the given amount of rows.
		for i in range(rows):
			#Create a row with the given number of pieces and append it to the list of rows.
			temp = BoardRow(pieces)
			self.rows.append(temp)
	def whipe(self):
		#Whipes all pieces from the rows of this column.
		for i in range(self.rows):
			self.rows[i].pieces = 0


class BoardRow:
	#This class does nothing except hold the pieces for the columns, which are on the board. In the future they might do something else, but for now it is just a simple class with an int.
	def __init__(self,pieces):
		self.pieces = pieces
