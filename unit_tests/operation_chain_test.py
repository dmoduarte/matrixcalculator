import unittest
from operations import operation_chain
from test_utils import MatrixCalculatorTestCases

class TestOperationChain(MatrixCalculatorTestCases):

    def test_operation_chain_size(self):
        operationChain = operation_chain.parseRequest(self.getRequestSample())
        self.assertEqual(operationChain.getSize(), 3)
    
    def test_operation_chain_iterable_iterations(self):
        operationChain = operation_chain.parseRequest(self.getRequestSample())
        iterations = 0

        for operation in operationChain:
            iterations += 1

        self.assertEqual(3, iterations)    

    def test_operation_chain_iterable_elements(self):
        operationChain = operation_chain.parseRequest(self.getRequestSample())
        
        for index, operation in enumerate(operationChain):
            if(index == 0):
                self.compareParsedAgainstRequestSample(
                    operation,
                    0, 
                    1, 
                    2
                )
            elif(index == 1):
                self.compareParsedAgainstRequestSample(
                    operation,
                    2, 
                    3, 
                    4
                )   
            elif(index == 2):
                 self.compareParsedAgainstRequestSample(
                    operationChain.getOperationAtIndex(2), 
                    4, 
                    5, 
                    6
                )

    def test_operation_chain_elements(self):
        operationChain = operation_chain.parseRequest(self.getRequestSample())
 
        self.compareParsedAgainstRequestSample(
            operationChain.getOperationAtIndex(0),
            0, 
            1, 
            2
        )

        self.compareParsedAgainstRequestSample(
            operationChain.getOperationAtIndex(1),
            2, 
            3, 
            4
        )

        self.compareParsedAgainstRequestSample(
            operationChain.getOperationAtIndex(2), 
            4, 
            5, 
            6
        )
   
if __name__ == '__main__':
    unittest.main()