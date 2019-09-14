import unittest
from matrix import Matrix
from operations import *

class TestCalculatorOperations(unittest.TestCase):

    def test_matrix_addition(self):
        m1 = Matrix({'1': {'1': 1, '2': 3}, '2': {'1': 3, '2': 4}})
        m2 = Matrix({'1': {'1': 2, '2': 3}, '2': {'1': 4, '2': 4}})
        m3 = add(m1, m2)

        self.assertEqual(m3.matrix, {
            '1': {'1': 3, '2': 6},
            '2': {'1': 7, '2': 8}
        })

    def test_matrix_scalar_multiplication(self):
        m1 = Matrix({'1': {'1': 1, '2': 3}, '2': {'1': 3, '2': 4}})
        m2 = multiplyWithScalar(m1, 3)

        self.assertEqual(m2.matrix, {
            '1': {'1': 3, '2': 9},
            '2': {'1': 9, '2': 12}
        })

    def test_matrix_matrix_multiplication(self):
        m1 = Matrix({
            '1': {'1': 1, '2': 0, '3': -3},
            '2': {'1': -2, '2': 4, '3': 1}
        })
        
        m2 = Matrix({
            '1': {'1': 1, '2': 0, '3': 4, '4': 1},
            '2': {'1': -2, '2': 3, '3': -1, '4': 5},
            '3': {'1': 0, '2': -1, '3': 2, '4': 1}
        })

        m3 = multiplyMatrices(m1, m2)

        self.assertEqual(m3.matrix, {
            '1': {'1': 1, '2': 3, '3': -2, '4': -2},
            '2': {'1': -10, '2': 11, '3': -10, '4': 19}
        })


if __name__ == '__main__':
    unittest.main()
