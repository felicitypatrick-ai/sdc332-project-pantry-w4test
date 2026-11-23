import unittest

from app.settings import SATURDAY_CAPACITY


class SettingsTests(unittest.TestCase):
    def test_capacity_is_a_positive_number(self):
        self.assertGreater(SATURDAY_CAPACITY, 0)
