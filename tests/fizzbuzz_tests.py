import unittest
from ..fizzbuzz_server.fizzbuzz_logic import get_result, get_stats


class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz_get_result(self):
        actual_result = get_result(3, 5, 15, 'fizz', 'buzz')
        expected_result = '1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz'
        self.assertEqual(actual_result, expected_result)

    def test_statistics(self):
        stats = get_stats()
        self.assertEqual(stats, {'stats message': 'No requests'})


if __name__ == '__main__':
    unittest.main()

