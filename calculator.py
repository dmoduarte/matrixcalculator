import json
from validator import *
from matrix import *

# Matrix addition: adds m1 with m2 bot with dimension = mxn, resulting in matrix m3 with dimension = mxn


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
    # Check the matrix validaty
    # Ensure matrix product is defined:
                # m1*m2 is only possible if dim(m1) = mxn and
                # dim(m2) = n*p. I.e the number of cols in m1 = number of rows in m2
                # if this is true then m1*m2 results in a matrix m3 where dim(m3) = m*p
    checkMatrixValidity(m1)
    checkMatrixValidity(m2)
    productDefinition = checkMatrixProduct(m1, m2)

m1 = Matrix({'1': {'1': 1, '2': 3}, '2': {'1': 3, '2': 4}})
m2 = Matrix({'1': {'1': 2, '2': 3}, '2': {'1': 4, '2': 4}})

print(json.dumps(vars(m1), indent=4))
print(json.dumps(vars(m2), indent=4))
print(json.dumps(vars(add(m1, m2)), indent=4))
print(json.dumps(vars(multiplyWithScalar(add(m1, m2), 2)), indent=4))
