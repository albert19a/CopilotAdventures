import unittest
from tempora.app import convert_time_to_minutes, sync_clocks
# launch automatic tests, runs all tests in the tests directory
# python -m unittest discover tests
# 
# Alertnativa per trovare il path: NON capisco il suggerimento, visto che dopo mi fa importare il full path
'''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tempora.app import sync_clocks
'''
class TestSyncClocks(unittest.TestCase):
    def test_sync_clocks(self):
        clock_times = ["14:45", "15:05", "15:00", "14:40"]
        expected_result = [-15, 5, 0, -20]
        grand_clock_time = "15:00"
        self.assertEqual(sync_clocks(clock_times, grand_clock_time), expected_result)

if __name__ == '__main__':
    unittest.main()
