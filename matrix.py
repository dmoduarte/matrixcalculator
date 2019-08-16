# Inverts the matrix representation.
# If the matrix representation is row => columns, by applying this function it'll change to column => rows
# This shall bean idempotent operation by returning a new matrix i.e does not change the argument matrix


def invertMatrixRepresentation(matrix):
    return {}


class Matrix:
    def __init__(self, matrixDict):
        self.matrix = matrixDict

    def setValueAt(self, i, j, value):
        #print(i, j, self.matrix, value);
        if i in self.matrix:
            self.matrix[i][j] = value
        else:
            newCell = {}
            newCell[j] = value
            self.matrix[i] = newCell

    def forEachCell(self, fn):
        for row, cols in self.matrix.items():
            for col, value in cols.items():
                cell = Cell(row, col, value)
                fn(cell)

    def getValueAt(self, i, j):
        return self.matrix[i][j]

    # return the dimension of the matrix mxn
    # {m:n}, where m is the number of rows and n the cols
    # assumes the matrix representation is valid
    def dim(self):
        dim = {}
        dim['m'] = len(self.matrix)
        dim['n'] = len(self.matrix.values()[0])
        return dim


class Cell:
    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value

    def getRow(self):
        return self.row

    def getColumn(self):
        return self.column

    def getValue(self):
        return self.value
