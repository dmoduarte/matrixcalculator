from enum import Enum
import heapq
from matrix import Matrix
from operations import operation_chain, operations

class OperatorRank(Enum):
    KMULT = 4
    MULT = 3
    ADD = 2
    SUB = 1

def consumeRequest(request):
    operationChain = operation_chain.parseRequest(request)
    
    #todo: validate chain
    
    operationsInPrecedence = createPrecedenceArray(operationChain)
    
    result = Matrix({})

    for i in range(len(operationsInPrecedence)):
        operation = heapq.heappop(operationsInPrecedence)[2]

        result = operations.delegateOperation(
            Matrix(operation.getLeftOperand()),
            Matrix(operation.getRightOperand()),
            operation.getOperator()['op']
        )

        operation.setCalculated(True)
        
        if operation.previous is not None and not operation.previous.isCalculated():
            operation.previous.setRightOperand(result.matrix)

        if operation.next is not None and not operation.next.isCalculated():
            operation.next.setLeftOperand(result.matrix)
        
    return result.matrix

def createPrecedenceArray(operationChain):
    heap = []
    for operationRequest in operationChain:
        operationPriority = -1 * OperatorRank[operationRequest.getOperator()['op']].value

        heapq.heappush(
            heap, (operationPriority, operationRequest.getPositionInChain(), operationRequest)
        )

    return heap    