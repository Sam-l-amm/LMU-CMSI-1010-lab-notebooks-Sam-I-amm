"""
Grading Unit Tests for highroller.py
Run this file to check your work!
You should not modify this file.
"""

import unittest
from highroller import Die, DiceSet


class DieTests(unittest.TestCase):

    def test_init(self):
        d = Die(3, 6)  # 6-sided die with initial value 3
        self.assertEqual(d.get_number_sides(), 6)
        self.assertEqual(d.get_current_value(), 3)

    def test_roll(self):
        d1 = Die(3, 6)  # 6-sided die with initial value 3
        d1_new_value = d1.roll()
        self.assertTrue(1 <= d1.get_current_value() <= 6)

        # The new value should be returned by roll()
        self.assertTrue(d1_new_value is not None)
        self.assertEqual(d1_new_value, d1.get_current_value())

        d2 = Die(1, 20)
        d2_new_value = d2.roll()
        self.assertTrue(1 <= d2.get_current_value() <= 20)
        self.assertTrue(d2_new_value is not None)
        self.assertEqual(d2_new_value, d2.get_current_value())

    def test_str(self):
        d1 = Die(3, 6)  # 6-sided die with initial value 3
        self.assertEqual(str(d1), "[3]")

        d2 = Die(1, 5)  # 5-sided die with initial value 1
        self.assertEqual(str(d2), "[1]")

        d3 = Die(5, 20)  # 20-sided die with initial value 5
        d3.roll()
        self.assertEqual(str(d3), f"[{d3.get_current_value()}]")


class DiceSetTests(unittest.TestCase):

    def test_init(self):
        ds = DiceSet(3, 6)  # 6 dice, each with 3 sides
        values = ds.get_current_values()

        # This DiceSet should have 6 dice
        self.assertEqual(len(values), 6)
        # All dice should be initialized to 1
        self.assertTrue(all(value == 1 for value in values))

    def test_descriptor(self):
        ds = DiceSet(5, 3)  # 3 dice, each with 5 sides
        self.assertEqual(ds.get_descriptor(), "3d5")

        ds = DiceSet(20, 1)  # 1 die with 20 sides
        self.assertEqual(ds.get_descriptor(), "1d20")

    def test_get_total(self):
        ds = DiceSet(3, 6)  # 6 dice, each with 3 sides

        # All dice start off as 1, so the total should be 6
        self.assertEqual(ds.get_total(), 6)

        ds.roll_all()
        new_values = ds.get_current_values()
        # The total should be the sum of the new values
        self.assertEqual(ds.get_total(), sum(new_values))

    def test_roll_all(self):
        ds = DiceSet(3, 6)  # 6 dice, each with 3 sides
        ds.roll_all()
        values = ds.get_current_values()
        self.assertTrue(all(1 <= value <= 6 for value in values))

    def test_roll_die(self):
        ds = DiceSet(10, 6)  # 6 dice, each with 10 sides
        old_values = ds.get_current_values()

        new_die_value = ds.roll_die(0)  # Roll the first die at index 0
        new_values = ds.get_current_values()

        # Die 0 should be between 1 and 10
        self.assertTrue(1 <= ds.get_current_values()[0] <= 10)
        # The other dice should not have changed
        self.assertEqual(old_values[1:], new_values[1:])

        # The new die value should have been returned
        self.assertTrue(new_die_value is not None)
        self.assertTrue(new_values[0] == new_die_value)

    def test_str(self):
        ds = DiceSet(3, 4)  # 4 dice, each with 3 sides
        self.assertEqual(str(ds), "[1][1][1][1]")

        ds.roll_all()
        new_values = ds.get_current_values()
        dice_str = str(ds)

        # Check that the string representation is correct
        for i in range(len(new_values)):
            self.assertEqual(f"[{new_values[i]}]", dice_str[i * 3: i * 3 + 3])


# Run the unit tests
if __name__ == "__main__":
    unittest.main()
