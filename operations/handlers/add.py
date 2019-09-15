import base
from matrix import Matrix
import validator

class Add(base.OperationHandler):
    
    def validateOperation(self, operation):
        m1 = operation.getLeftOperand() 
        m2 = operation.getRightOperand()

        validator.checkMatrixValidity(m1)
        validator.checkMatrixValidity(m2)
        validator.checkEqualSize(m1, m2)

    def calculateOperation(self, operation):
        # Alghorithm:
        # ensure dim(m1) == dim(m2) i,e if m1 is of size mXn then m2 should be mXn as well
        # then m3 = m1 + m2 results from m3ij = m1ij + m2ij where i and j are both coordinates from each matrix:
                    # create a new Matrix m3
                    # iterate over each element ij of m1
                            #m3ij = m1ij + m2ij
        m3 = Matrix({})

        m1 = operation.getLeftOperand()
        m2 = operation.getRightOperand()

        m1.forEachCell(lambda m1Cell: m3.setValueAt(m1Cell.getRow(), m1Cell.getColumn(),
                                                    m1Cell.getValue() + m2.getValueAt(m1Cell.getRow(), m1Cell.getColumn())))

        return m3
