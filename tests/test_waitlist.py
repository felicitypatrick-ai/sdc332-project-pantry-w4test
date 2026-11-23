import unittest

from app.waitlist import waitlist_position


class LineTests(unittest.TestCase):
    def test_first_is_number_one(self):
        self.assertEqual(waitlist_position(["Garcia", "Nguyen", "Okafor"], "Garcia"), 1)

    def test_not_on_list_gets_zero(self):
        self.assertEqual(waitlist_position(["Garcia", "Nguyen"], "Okafor"), 0)

    def test_third_is_number_three(self):
        self.assertEqual(waitlist_position(["Garcia", "Nguyen", "Okafor"], "Okafor"), 3)
