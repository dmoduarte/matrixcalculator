class OperationChain:

    def __init__(self):
        self.head = None
        self.tail = None
        self.nextOp = None
        self.idx = 0
        self.size = 0

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

    def getOperationAtIndex(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        idx = 0
        currentNode = self.head
        while(currentNode is not None and idx < index):
            currentNode = currentNode.next
            idx += 1
            
        return currentNode

    ####
    def addBack(self, operation):
        if self.head is None and self.tail is None:
            self.head = operation
            self.tail = operation
        else:
            operation.previous = self.tail
            self.tail.next = operation
            self.tail = operation

        self.size += 1	
    
    def getSize(self):
        return self.size

    class OperationRequest:
        def __init__(self, operator, leftOperand, rightOperand):
            self.operator = operator
            self.leftOperand = leftOperand
            self.rightOperand = rightOperand
            self.next = None
            self.previous = None

        def setPrevious(self, operationRequest):
            self.previous = operationRequest

        def setNext(self, operationRequest):
            self.next = operationRequest

        def setResult(self, result):
            self.result = result

        def getOperator(self):
            return self.operator	

        def getResult(self):
            return self.result 

def parseRequest(request):

    operationChain = OperationChain()
    for index, item in enumerate(request):
        if index == len(request) - 2:
            break 

        if isOperator(item):
            continue

        leftOperand = request[index]
        operator = request[index+1]
        rightOperand = request[index+2]	
        
        operationChain.addBack(OperationChain.OperationRequest(operator, leftOperand, rightOperand))
    
    return operationChain

def isOperator(item):
    return "op" in item