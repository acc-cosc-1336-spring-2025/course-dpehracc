#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

import unittest
from src.homework.j_classes.class_a import Die

class TestDie(unittest.TestCase):
    def test_die_roll_within_range(self):
        die = Die()
        for _ in range(3):
            die.roll()
            value = die.get_rolled_value()
            self.assertIn(value, range(1, 7), f"The roll was out of range: {value}")
            