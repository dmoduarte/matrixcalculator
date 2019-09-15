import unittest
from request_samples import *

class MatrixCalculatorTestCases(unittest.TestCase):

    def getRequestSample(self, **sample):
        chosenSample = sample.get('sample') 

        samples = {
            "A":requestSampleA,
            "B":requestSampleB,
            "C":requestSampleC
        }

        return requestSampleA if chosenSample is None else samples[chosenSample]

    def compareParsedAgainstRequestSample(self,
                                            parsedOp,
                                            leftRequestedOpIdx,
                                            requestedOpIdx,
                                            rightRequestedOpIdx,
                                            **sample):

        chosenSample = self.getRequestSample(sample = sample.get("sample")) 

        self.assertDictEqual(
            parsedOp.leftOperand,
            chosenSample[leftRequestedOpIdx]
        )

        self.assertDictEqual(
            parsedOp.operator,
            chosenSample[requestedOpIdx]
        )

        self.assertDictEqual(
            parsedOp.rightOperand,
            chosenSample[rightRequestedOpIdx]
        )