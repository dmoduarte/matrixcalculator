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

	def setPrevious(previousOperation):
		self.prevOp = previousOperation

	def setNext(nextOperation):
		self.nextOp = nextOperation	
		
def consumeRequest(request):
   operationChain = buildOperationChain(request)

def buildOperationChain(request):
	head = None

	previousRequest = None
	for index, item in enumerate(request):
		if isOperator(item):
			continue

		matrix1 = request[index]
		operator = request[index+1]
		matrix2 = request[index+2]

		opRequest = OperationRequest(operator, matrix1, matrix2)

		if head is None:
			head = opRequest

		if previousRequest is not None:
			opRequest.setPrevious(previousRequest)
			previousRequest.setNext(opRequest)	

	return head

def isOperator(item): 
	return "op" in item