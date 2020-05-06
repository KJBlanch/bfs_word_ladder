from unittest import TestCase


class TestFortesting_1(TestCase):
    def test_fortesting_1(self):
        self.fail()

    def test_input(self):
        self.assertRaises(fortesting_1(lead, gold, dictionary, "", "", 1))