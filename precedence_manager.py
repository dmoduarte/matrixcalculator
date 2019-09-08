from enum import Enum, auto
from heapq import *
from util import linked_list
from operation_chain import *


class OperatorRank(Enum):
    KMULT = 4
    MULT = 3
    ADD = 2
    SUB = 1


def consumeRequest(request):
    operationChain = parseRequest(request)

    #build heap
    heap = []
    for operationRequest in operationChain:
        operationPriority = OperatorRank[operationRequest.getOperator()]

        heapq.heappush(
            heap, (operationPriority, operationRequest)
        )

    print(heapq)
