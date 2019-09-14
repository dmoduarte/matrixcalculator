from enum import Enum
import heapq
from matrix import Matrix
from operations import operation_chain, delegate

class OperatorRank(Enum):
    KMULT = 4
    MULT = 3
    ADD = 2
    SUB = 1

def consumeRequest(request):
    operationChain = operation_chain.parseRequest(request)
    #validate chain
    operationsInPrecedence = createPrecedenceArray(operationChain)
    result = Matrix({})

    for i in range(len(operationsInPrecedence)):
        operation = heapq.heappop(operationsInPrecedence)

        result = delegate.calculateOperation(operation)

        operation.setCalculated(True)
        
        if operation.previous is not None and not operation.previous.isCalculated():
            operation.previous.setRightOperand(result)

        if operation.next is not None and not operation.next.isCalculated():
            operation.next.setLeftOperand(result)
        
    return result

def createPrecedenceArray(operationChain):
    heap = []
    for operationRequest in operationChain:
        operationPriority = -1 * OperatorRank[operationRequest.getOperator()['op']].value
        print( "%s = %s" % (OperatorRank[operationRequest.getOperator()['op']], operationPriority) )
        heapq.heappush(
            heap, (operationPriority, operationRequest.getPositionInChain(), operationRequest)
        )

    return heap    