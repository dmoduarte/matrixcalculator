import unittest

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

class MatrixCalculatorTestCases(unittest.TestCase):

    def getRequestSample(self):
        return requestSample

    def compareParsedAgainstRequestSample(self,
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