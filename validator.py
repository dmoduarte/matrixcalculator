def checkEqualSize(m1, m2):
    if not areEqualSize(m1, m2):
        raise ValueError("m1 and m2 do not have the same dimension")


def checkMatrixValidity(m):
    firstRowLen = len(list(m.matrix.values())[0])
    sliced = list(m.matrix.values())[1:]
    for row in sliced:
        if len(row) != firstRowLen:
            raise ValueError("Matrix is not valid")
            #todo: check if row -> col is sequential

# Checks if matrix product between m1 and m2 is defined
# If dim(m1) = mxn and dim(m2) = nxp then the product is defined.
# In such case this function shall return an object {rows:n, cols:p}
# Representing then dimension of matrix result from multipkying m1 and m2
# If no product is defined, this function raises a ValueError


def checkMatrixProduct(m1, m2):
    dimM1 = m1.dim()
    dimM2 = m2.dim()

    if dimM1['n'] != dimM2['m']:
    	raise ValueError('Matrix product not defined')

    return

# checks if m1 and m2 have the same dimension i.e both have dimension = mxn


def areEqualSize(m1, m2):
    m1Dim = m1.dim()
    m2Dim = m2.dim()
    return m1Dim['m'] == m2Dim['m'] and m1Dim['n'] == m2Dim['n']
