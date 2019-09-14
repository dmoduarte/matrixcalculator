import unittest
from operations import operation_chain

requestSample = [
    {
        "1": {"1": 1, "2": 3},
        "2": {"1": 3, "2": 4}
    },

    {"op": "ADD"},

    {
        "1": {"1": 2, "2": 3},
        "2": {"1": 4, "2": 4}
    },

    {"op": "ADD"},

    {
        "1": {"1": 1, "2": 0, "3": -3},
         "2": {"1": -2, "2": 4, "3": 1}
    },

    {"op": "MULT"},

    {
        "1": {"1": 1, "2": 0, "3": 4, "4": 1},
        "2": {"1": -2, "2": 3, "3": -1, "4": 5},
        "3": {"1": 0, "2": -1, "3": 2, "4": 1}
    }
]

class TestOperationChain(unittest.TestCase):

    def test_operation_chain_size(self):
        operationChain = operation_chain.parseRequest(requestSample)
        self.assertEqual(operationChain.getSize(), 3)
    
    def test_operation_chain_iterable_iterations(self):
        operationChain = operation_chain.parseRequest(requestSample)
        iterations = 0

        for operation in operationChain:
            iterations += 1

        self.assertEqual(3, iterations)    

    def test_operation_chain_iterable_elements(self):
        operationChain = operation_chain.parseRequest(requestSample)
        
        for index, operation in enumerate(operationChain):
            if(index == 0):
                self.compareParsedAgainstRequestedOperations(
                    operation,
                    0, 
                    1, 
                    2
                )
            elif(index == 1):
                self.compareParsedAgainstRequestedOperations(
                    operation,
                    2, 
                    3, 
                    4
                )   
            elif(index == 2):
                 self.compareParsedAgainstRequestedOperations(
                    operationChain.getOperationAtIndex(2), 
                    4, 
                    5, 
                    6
                )

    def test_operation_chain_elements(self):
        operationChain = operation_chain.parseRequest(requestSample)
 
        self.compareParsedAgainstRequestedOperations(
            operationChain.getOperationAtIndex(0),
            0, 
            1, 
            2
        )

        self.compareParsedAgainstRequestedOperations(
            operationChain.getOperationAtIndex(1),
            2, 
            3, 
            4
        )

        self.compareParsedAgainstRequestedOperations(
            operationChain.getOperationAtIndex(2), 
            4, 
            5, 
            6
        )

    def compareParsedAgainstRequestedOperations(self,
                                                parsedOp,
                                                leftRequestedOpIdx,
                                                requestedOpIdx,
                                                rightRequestedOpIdx):    
        self.assertDictEqual(
            parsedOp.leftOperand,
            requestSample[leftRequestedOpIdx]
        )

        self.assertDictEqual(
            parsedOp.operator,
            requestSample[requestedOpIdx]
        )
        
        self.assertDictEqual(
            parsedOp.rightOperand,
            requestSample[rightRequestedOpIdx]
        )
   
if __name__ == '__main__':
    unittest.main()