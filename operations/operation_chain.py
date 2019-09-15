class OperationChain:

    def __init__(self):
        self.head = None
        self.tail = None
        self.currentOp = None
        self.iterating = False
        self.size = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.currentOp is not None and self.currentOp.getNext() is None and self.iterating:
            self.iterating = False
            raise StopIteration

        elif self.currentOp is None and not self.iterating:
            self.currentOp = self.head
            self.iterating = True
            return self.currentOp
        
        self.currentOp = self.currentOp.getNext()
        self.iterating = True
        return self.currentOp

    def getOperationAtIndex(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        idx = 0
        currentNode = self.head
        while(currentNode is not None and idx < index):
            currentNode = currentNode.next
            idx += 1
            
        return currentNode    

    def addBack(self, operation):
        if self.head is None and self.tail is None:
            self.head = operation
            self.tail = operation
        else:
            operation.previous = self.tail
            self.tail.next = operation
            self.tail = operation

        operation.setPositionInChain(self.size)
        self.size += 1	
    
    def commit(self, operation):
        if operation.previous is not None:
            operation.previous.setRightOperand(operation.getResult())
            operation.previous.next = operation.next

        if operation.next is not None:
            operation.next.setLeftOperand(operation.getResult())
            operation.next.previous = operation.previous

        operation.previous = None 
        operation.next = None   
        del operation

    def getSize(self):
        return self.size

    class OperationRequest:
        def __init__(self, operator, leftOperand, rightOperand):
            self.operator = operator
            self.leftOperand = leftOperand
            self.rightOperand = rightOperand
            self.next = None
            self.previous = None
            self.positionInChain = -1
            self.result = None

        def setPrevious(self, operationRequest):
            self.previous = operationRequest

        def setNext(self, operationRequest):
            self.next = operationRequest

        def setLeftOperand(self, leftOperand):
            self.leftOperand = leftOperand

        def setRightOperand(self, rightOperand):
            self.rightOperand = rightOperand  

        def setPositionInChain(self, position):
             self.positionInChain = position      

        def setResult(self, result):
            self.result = result

        def getNext(self):
            return self.next

        def getPrevious(self):
            return self.previous        

        def getOperator(self):
            return self.operator	

        def getLeftOperand(self):
            return self.leftOperand

        def getRightOperand(self):
            return self.rightOperand 

        def getPositionInChain(self):
            return self.positionInChain;       

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