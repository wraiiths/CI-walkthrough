import unittest
from capacity import remaining_seats


class CapacityTests(unittest.TestCase):
    def test_partly_booked(self):
        self.assertEqual(remaining_seats(10, 3), 7)

    def test_full(self):
        self.assertEqual(remaining_seats(10, 10), 0)

    def test_overbooked(self):
	    self.assertEqual(remaining_seats(10, 12), -2)
 
