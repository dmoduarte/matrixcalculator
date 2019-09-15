import base
from matrix import Matrix
import validator
from numbers import Number

class Multiply(base.OperationHandler):
    
    def validateOperation(self, operation):
        leftOperand = operation.getLeftOperand() 
        rightOperand = operation.getRightOperand()

        if(type(leftOperand) is Matrix):
            validator.checkMatrixValidity(leftOperand)
        elif (type(leftOperand) is not Number):   
            raise ValueError("leftOperand type is not supported") 

        if(type(rightOperand) is Matrix):
            validator.checkMatrixValidity(rightOperand)
        elif (type(leftOperand) is not Number):   
            raise ValueError("leftOperand type is not supported")     

        # Ensure matrix product is defined:
                # m1*m2 is only possible if dim(m1) = mxn and
                # dim(m2) = n*p. I.e the number of cols in m1 = number of rows in m2
                # if this is true then m1*m2 shall result in a matrix m3 where dim(m3) = m*p
        if(type(leftOperand) is Matrix and type(rightOperand) is Matrix):        
            validator.checkMatrixProduct(leftOperand, rightOperand)        

    def calculateOperation(self, operation):
        leftOperand = operation.getLeftOperand() 
        rightOperand = operation.getRightOperand()

        if(type(leftOperand) is Matrix and type(rightOperand) is Matrix):
            return multiplyMatrices(leftOperand, rightOperand)
        
        if(type(leftOperand) is Number):
            return multiplyWithScalar(rightOperand, leftOperand)
        
        return multiplyWithScalar(leftOperand, rightOperand)
        
def multiplyWithScalar(m1, k):
    # iterate over each element ij of m1
                        #m2ij = m1ij * k
    validator.checkMatrixValidity(m1)

    m2 = Matrix({})

    m1.forEachCell(lambda m1Cell: m2.setValueAt(m1Cell.getRow(), m1Cell.getColumn(), m1Cell.getValue() * k))

    return m2   

def multiplyMatrices(m1, m2):
    # Check the matrix validity
    # Ensure matrix product is defined:
                # m1*m2 is only possible if dim(m1) = mxn and
                # dim(m2) = n*p. I.e the number of cols in m1 = number of rows in m2
                # if this is true then m1*m2 shall result in a matrix m3 where dim(m3) = m*p

    # extract row vectors of m1
    # extract column vectors of m2
    # for each row vector of m1: rN
        # for each column vector of m2: cM
        # calculate product of rN and cM = rN.cM
        # insert rN.cM at position (N,M) of m3
    
    rowVectors = m1.extractRowVectors()
    columnVectors = m2.extractColumnVectors()

    m3 = Matrix({})

    rowVectorCount = 1
    for rowVector in rowVectors:
        columnVectorCount = 1
        
        for columnVector in columnVectors:
            dProd = dotProduct(rowVector, columnVector)
            m3.setValueAt(rowVectorCount, columnVectorCount, dProd)
            columnVectorCount += 1

        rowVectorCount += 1

    return m3

def dotProduct(vector1, vector2):
    return sum([vector1[i]*vector2[i] for i in range(len(vector1))])