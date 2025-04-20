#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory = {}
        add_inventory(inventory, "Widget1", 10)
        self.assertEqual(inventory["Widget1"], 10)

        add_inventory(inventory, "Widget1", 25)
        self.assertEqual(inventory["Widget1"], 35)

        add_inventory(inventory, "Widget1", -10)
        self.assertEqual(inventory["Widget1"], 25)

    def test_remove_inventory_widget(self):
        inventory = {"Widget1": 10, "Widget2": 20}
        result = remove_inventory_widget(inventory, "Widget1")
        self.assertEqual(result, "Record deleted")
        self.assertEqual(len(inventory), 1)
        self.assertIn("Widget2", inventory)

        result_not_found = remove_inventory_widget(inventory, "Nonexistent")
        self.assertEqual(result_not_found, "Item not found")