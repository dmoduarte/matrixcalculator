import unittest
from operation_chain import OperationChain, parseRequest

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
        operationChain = parseRequest(requestSample)
        self.assertEqual(operationChain.getSize(), 3)

    def test_operation_chain_elements(self):
        operationChain = parseRequest(requestSample)
        
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