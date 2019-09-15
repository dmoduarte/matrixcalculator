import unittest
import calculator
from operations import operation_chain
from test_utils import MatrixCalculatorTestCases
import heapq

class TestCalculator(MatrixCalculatorTestCases):
    def test_operations_precedence(self):
        operations = operation_chain.parseRequest(self.getRequestSample())
        
        precedenceArray = calculator.createPrecedenceArray(operations)
        
        self.compareParsedAgainstRequestSample(
            heapq.heappop(precedenceArray)[2],
            4,
            5,
            6
        )
    
        self.compareParsedAgainstRequestSample(
            heapq.heappop(precedenceArray)[2],
            0,
            1,
            2
        )
    
        self.compareParsedAgainstRequestSample(
            heapq.heappop(precedenceArray)[2],
            2,
            3,
            4
        )  

    def test_calculate_operations(self):      
        result = calculator.consumeRequest(self.getRequestSample()) 

        print(result)

if __name__ == '__main__':
    unittest.main()