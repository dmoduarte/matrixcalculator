import operations

def calculateOperation(operation):
    #route to operator handler and calculate
    return operationMapping()[operation.getOperator()](
            operation.getLeftOperand(),
            operation.getRightOperand()
        )

def operationMapping():
    return {
        'KMULT': operations.multiplyWithScalar,
        'MULT': operations.multiplyMatrices,
        'ADD': operations.add
    }