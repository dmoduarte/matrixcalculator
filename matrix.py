from numbers import Number


class Matrix:
    def __init__(self, matrixDict):
        self.matrix = matrixDict

    def setValueAt(self, i, j, value):
        i = str(i) if isinstance(i, Number) else i
        j = str(j) if isinstance(j, Number) else j

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
        i = str(i) if isinstance(i, Number) else i
        j = str(j) if isinstance(j, Number) else j
        return self.matrix[i][j]

    # return the dimension of the matrix mxn
    # {m:x, n:y}, where m is the number of rows and n the cols
    # assumes the matrix representation is valid
    def dim(self):
        dim = {}
        dim['m'] = len(self.matrix)
        dim['n'] = len(self.matrix.values()[0])
        return dim

    def extractRowVectors(self):
        dim = self.dim()
        vectors = [[0 for i in range(dim['n'])] for j in range(dim['m'])]

        def insertValueAt(cell): vectors[int(cell.getRow()) - 1][int(cell.getColumn()) - 1] = cell.getValue()
        self.forEachCell(insertValueAt)
      
        return vectors

    def extractColumnVectors(self):
        dim = self.dim()
        vectors = [[0 for i in range(dim['m'])] for j in range(dim['n'])]

        def insertValueAt(cell): vectors[int(cell.getColumn()) - 1][int(cell.getRow()) - 1] = cell.getValue()
        self.forEachCell(insertValueAt)

        return vectors


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
