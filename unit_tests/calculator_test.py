import unittest
import calculator
from operations import operation_chain
import heapq

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

class TestCalculator(unittest.TestCase):
    def test_operations_precedence(self):
        operations = operation_chain.parseRequest(requestSample)
        precedenceArray = calculator.createPrecedenceArray(operations)
        print(heapq.heappop(precedenceArray))

if __name__ == '__main__':
    unittest.main()