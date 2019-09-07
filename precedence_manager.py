from enum import Enum, auto
from util import linked_list


class Operations(Enum):
    KMULT = 4
    MULT = 3
    ADD = 2
    SUB = 1

class OperationRequest:
    def __init__(self, operator, matrix1, matrix2):
        self.operator = operator
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def setPrevious(operationRequest):
        self.previous = operationRequest

    def setNext(operationRequest):
        self.next = operationRequest

    def setResult(matrix):
    	self.result = matrix

    def getResult():
    	return self.result;

def consumeRequest(request):
    operationChain = buildOperationChain(request)

def buildOperationChain(request):
    head = None
    previousRequest = None

    for index, item in enumerate(request):

    	if index == len(request) - 2:
    		return 

    	if isOperator(item):
    		continue
    	
    	opRequest = buildOperationRequest(index, request)

    	if head is None:
    		head = opRequest	

    	if previousRequest is not None:
    		setDependency(previousRequest, opRequest)

    	previousRequest = opRequest

    return head

def buildOperationRequest(currentIndex, requestList):
	matrix1 = requestList[currentIndex]
	operator = requestList[currentIndex+1]
	matrix2 = requestList[currentIndex+2]

	return OperationRequest(operator, matrix1, matrix2)

def setDependency(previousOp, nextOp):
    previousOp.setNext(nextOp)
    nextOp.setPrevious(previousOp)

def isOperator(item):
    return "op" in item
