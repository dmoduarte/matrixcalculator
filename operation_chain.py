class OperationChain:

	def __init__(self):
		self.idx = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.nextOp is None and self.idx > 0:
			self.idx = 0
			raise StopIteration

		if self.nextOp is None and self.idx == 0:
			self.nextOp = self.head
			self.idx += 1
			return self.nextOp
		
		next = self.nextOp
		self.nextOp = self.nextOp.next
		self.idx += 1
		return next

	def addBack(operartion):
		if self.head is None and self.tail is None:
			self.head = self.tail = operation
		else:
			operation.previous = self.tail
			self.tail = self.tail.next = operation

	class OperationRequest:
	    def __init__(self, operator, leftOperand, rightOperand):
	        self.operator = operator
	        self.leftOperand = leftOperand
	        self.rightOperand = rightOperand

	    def setPrevious(operationRequest):
	        self.previous = operationRequest

	    def setNext(operationRequest):
	        self.next = operationRequest

	    def setResult(result):
	    	self.result = result

	    def getOperator():
	    	return self.operator;	

	    def getResult():
	    	return self.result 

def parseRequest(request):
    operationChain = OperationChain()

    for index, item in enumerate(request):

    	if index == len(request) - 2:
    		return 

    	if isOperator(item):
    		continue

    	leftOperand = request[index]
    	operator = request[index+1]
    	rightOperand = request[index+2]	
    	
    	operationChain.addBack(OperationRequest(operator, leftOperand, rightOperand))

    return operationChain

def isOperator(item):
    return "op" in item