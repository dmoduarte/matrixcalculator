import json
from validator import *
from matrix import *

# Matrix addition: adds m1 with m2 both with dimension = mxn, resulting in matrix m3 with dimension = mxn


def add(m1, m2):
    # Alghorithm:
    # ensure dim(m1) == dim(m2) i,e if m1 is of size mXn then m2 should be mXn as well
    # then m3 = m1 + m2 results from m3ij = m1ij + m2ij where i and j are both coordinates from each matrix:
                # create a new Matrix m3
                # iterate over each element ij of m1
                        #m3ij = m1ij + m2ij
    checkMatrixValidity(m1)
    checkMatrixValidity(m2)
    checkEqualSize(m1, m2)

    m3 = Matrix({})

    m1.forEachCell(lambda m1Cell: m3.setValueAt(m1Cell.getRow(), m1Cell.getColumn(),
                                                  m1Cell.getValue() + m2.getValueAt(m1Cell.getRow(), m1Cell.getColumn())))

    return m3

# Scalar multiplication: multiplies a matrix m1, with dimension = mxn, with a scalar k, resulting in a matrix m2 with dimension = mxn


def multiplyWithScalar(m1, k):
    # Alghorithm:
    # iterate over each element ij of m1
                        #m2ij = m1ij * k
    checkMatrixValidity(m1)

    m2 = Matrix({})

    m1.forEachCell(lambda m1Cell: m2.setValueAt(m1Cell.getRow(), m1Cell.getColumn(), m1Cell.getValue() * k))

    return m2


def multiplyMatrices(m1, m2):
    # Alghorithm
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

    checkMatrixValidity(m1)
    checkMatrixValidity(m2)
    
    # check product definition
    # productDefinition = checkMatrixProduct(m1, m2)

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

    return m3;

def dotProduct(vector1, vector2):
    return sum([vector1[i]*vector2[i] for i in range(len(vector1))])


m1 = Matrix({'1': {'1': 1, '2': 3}, '2': {'1': 3, '2': 4}})
m2 = Matrix({'1': {'1': 2, '2': 3}, '2': {'1': 4, '2': 4}})

#print(json.dumps(vars(m1), indent=4))
#print(json.dumps(vars(m2), indent=4))
#print(json.dumps(vars(add(m1, m2)), indent=4))
#print(json.dumps(vars(multiplyWithScalar(add(m1, m2), 2)), indent=4))
