import unittest
from mobile_network.counter import count_unreachable


class TestTotalWork(unittest.TestCase):
    def test_output(self):
        test_data = [
            ([[['A', 'B'], ['B', 'C'], ['C', 'D']],
              {'A': 10, 'B': 20, 'C': 30, 'D': 40},
              'A', ['C']], 70),
            ([[['A', 'B'], ['B', 'D'], ['A', 'C'], ['C', 'D']],
              {'A': 10, 'B': 0, 'C': 0, 'D': 40},
              'A', ['B']], 0),
            ([[['A', 'B']],
              {'A': 10, 'B': 0},
              'A', []], 0)
        ]
        for inputs, output in test_data:
            self.assertEqual(count_unreachable(*inputs), output)

    def test_incorrect_input(self):
        self.assertRaises(ValueError, count_unreachable,
                          [['A', 'B']], {'A': 10, 'C': 0}, 'A', [])


if __name__ == '__main__':
    unittest.main()
