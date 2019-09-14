from operations import multiplyMatrices, multiplyWithScalar, add

def calculateOperation(operation):
    #route to operator handler and calculate
    return operationMapping()[operation.getOperator()](
            operation.getLeftOperand(),
            operation.getRightOperand()
        )

def operationMapping():
    return {
        'KMULT': multiplyWithScalar,
        'MULT': multiplyMatrices,
        'ADD': add
    }