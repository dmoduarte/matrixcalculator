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
        result = calculator.consumeRequest(self.getRequestSample(sample="C")) 

        expectedResult = {
            '1': {'1': 10}
        }

        self.assertDictEqual(
            result,
            expectedResult
        )

        newSample = self.getRequestSample(sample="C").copy()

        newSample += [
            {"op": "MULT"},

            {
                "1": {"1": 2}
            }
        ]

        result = calculator.consumeRequest(newSample)

        expectedResult = {
            '1': {'1': 14}
        }

        self.assertDictEqual(
            result,
            expectedResult
        )

        result = calculator.consumeRequest(self.getRequestSample(sample="B")) 
        
        expectedResult = {
            '1': {'1': 109, '2': 34},
            '2': {'1': 142, '2': 42}
        }
        
        self.assertDictEqual(
            result,
            expectedResult
        )

if __name__ == '__main__':
    unittest.main()