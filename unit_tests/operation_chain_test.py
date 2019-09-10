import unittest
from operation_chain import OperationChain, parseRequest, isOperator

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
        operation = operationChain.getOperationAtIndex(0)

        self.assertOperationElementEquality(
            operation.leftOperand,
            requestSample[0]
        )

        self.assertOperationElementEquality(
            operation.operator,
            requestSample[1]
        )

        self.assertOperationElementEquality(
            operation.rightOperand,
            requestSample[2]
        )

        #print(operationChain.getSize())

        operation = operationChain.getOperationAtIndex(1)

        self.assertOperationElementEquality(
            operation.leftOperand,
            requestSample[2]
        )

        self.assertOperationElementEquality(
            operation.operator,
            requestSample[3]
        )

        self.assertOperationElementEquality(
            operation.rightOperand,
            requestSample[4]
        )
 

    def assertOperationEquality(self, operationChain, position):
        operation = operationChain.getOperationAtIndex(position)

        self.assertOperationElementEquality(
            operation.leftOperand,
            requestSample[position]
        )

        self.assertOperationElementEquality(
            operation.operator,
            requestSample[position+1]
        )

        self.assertOperationElementEquality(
            operation.rightOperand,
            requestSample[position+2]
        )

    def assertOperationElementEquality(self, parsed, request):
        self.assertDictEqual(parsed, request)         

if __name__ == '__main__':
    unittest.main()