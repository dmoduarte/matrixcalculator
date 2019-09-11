from enum import Enum, auto
import heapq
from operation_chain import *
from calculator import multiplyWithScalar, multiplyMatrices, add
from pyOptional import Optional

class OperatorRank(Enum):
    KMULT = 4
    MULT = 3
    ADD = 2
    SUB = 1

class OperationDelegate:
    @staticmethod
    def calculateOperation(operation):
        return OperationDelegate.operationMapping()[operation](
                operation.getLeftOperand(),
                operation.getRightOperand()
            )
            
    @staticmethod
    def operationMapping():
        return {
            'KMULT': multiplyWithScalar,
            'MULT': multiplyMatrices,
            'ADD': add
        }

def consumeRequest(request):
    operationChain = parseRequest(request)

    operationsInPrecedence = createPrecedenceArray(operationChain)

    for operation in operationsInPrecedence:
        result = OperationDelegate.calculateOperation(operation)
        
        Optional(operation.previous).if_present(lambda operation: operation.setRightOperand(result))

        Optional(operation.next).if_present(lambda operation: operation.setLeftOperand(result))    

def createPrecedenceArray(operationChain):
    heap = []
    for operationRequest in operationChain:
        operationPriority = OperatorRank[operationRequest.getOperator()]

        heapq.heappush(
            heap, (operationPriority, operationRequest)
        )

    return heap    