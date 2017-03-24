import unittest
from src.chrono import Chrono
from datetime import datetime

class test(unittest.TestCase):
    def test_single_expression(self):
        chrono = Chrono()

        string = 'now'
        result = chrono.parse(string, datetime(2016, 12, 2, 12))
        self.assertEqual(result, datetime(2016, 12, 2, 12))

        string = 'tomorrow'
        result = chrono.parse(string, datetime(2016, 12, 2, 12))
        self.assertEqual(result, datetime(2016, 12, 3, 12))

        string = 'yesterday'
        result = chrono.parse(string, datetime(2016, 12, 2, 12))
        self.assertEqual(result, datetime(2016, 12, 1, 12))

        string = 'tonight'
        result = chrono.parse(string, datetime(2016, 12, 2, 12))
        self.assertEqual(result, datetime(2016, 12, 2, 22))

        string = 'tomorrow night'
        result = chrono.parse(string, datetime(2016, 12, 2, 12))
        self.assertEqual(result, datetime(2016, 12, 3, 22))

        string = 'yesterday evening'
        result = chrono.parse(string, datetime(2016, 12, 2, 12))
        self.assertEqual(result, datetime(2016, 12, 1, 18))



if __name__ == '__main__':
    unittest.main()
