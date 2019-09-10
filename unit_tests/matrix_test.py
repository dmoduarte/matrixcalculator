import unittest
from matrix import Matrix

class TestMatrix(unittest.TestCase):

    def test_get_value_at(self):
        matrix = Matrix({'1': {'1': 3}, '2': {'1': 4}})
        self.assertEqual(matrix.getValueAt('2', '1'), 4)
        self.assertEqual(matrix.getValueAt(1, 1), 3)

    def test_set_value_at(self):
        matrix = Matrix({'1': {'1': 3}, '2': {'1': 4}})
        self.assertEqual(matrix.matrix, {'1': {'1': 3}, '2': {'1': 4}})
        matrix.setValueAt(1, 1, 5)
        self.assertEqual(matrix.matrix, {'1': {'1': 5}, '2': {'1': 4}})

    def test_get_dim(self):
        matrix = Matrix({
            '1': {'1': 3, '2': 4, '3': 6},
            '2': {'1': 4, '2': 5, '3': 9}
        })
        self.assertEqual(matrix.dim(), {'m': 2, 'n': 3})

if __name__ == '__main__':
    unittest.main()