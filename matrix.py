class Matrix:
	def __init__(self, matrixDict):
		self.matrix = matrixDict

	def setValueAt(self, i, j, value):
		#print(i, j, self.matrix, value);
		if i in self.matrix:
			self.matrix[i][j] = value;
		else:
			newCell = {};
			newCell[j] = value;
			self.matrix[i] = newCell;

	def getValueAt(self, i, j):
		return self.matrix[i][j];	

	# return the dimension of the matrix mxn
	# {m:n}, where m is the number of rows and n the cols
	# assumes the matrix representation is valid
	def dim(self):
		dim = {};
		dim['m'] = len(self.matrix);
		dim['n'] = len(self.matrix.values()[0]);    
		return dim;

	# returns key value pairs, where key is the row and value is the column and the cell
	def items(self):
		return self.matrix.items();