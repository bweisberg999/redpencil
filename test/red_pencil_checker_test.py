import unittest
from src import red_pencil_checker
import datetime


class MyTestCase(unittest.TestCase):
    original = 100

    def test_ifReductionIsLessThan5PercentThereIsNoRedPencilPromo(self):
        new = 96
        self.assertEqual(False, red_pencil_checker.is_promo_active(self.original, new))

    def test_ifReductionIsEqualTo5PercentThereIsARedPencilPromo(self):
        new = 95
        self.assertEqual(True, red_pencil_checker.is_promo_active(self.original, new))

    def test_ifReductionIsGreaterThan5PercentThereIsARedPencilPromo(self):
        new = 94
        self.assertEqual(True, red_pencil_checker.is_promo_active(self.original, new))

    def test_ifReductionIsGreaterThan30PercentThereIsNoRedPencilPromo(self):
        new = 69
        self.assertEqual(False, red_pencil_checker.is_promo_active(self.original, new))

    def test_ifReductionIsEqualTo30PercentThereIsARedPencilPromo(self):
        new = 70
        self.assertEqual(True, red_pencil_checker.is_promo_active(self.original, new))

    def test_ifReductionIsLessThan30PercentThereIsARedPencilPromo(self):
        new = 71
        self.assertEqual(True, red_pencil_checker.is_promo_active(self.original, new))

    def test_ifPriceHasChangedWithin30DaysGivenAValidReductionThereIsNoRedPencilPromo(self):
        new = 71
        lastchanged = datetime.date(1, 1, 1)
        


if __name__ == '__main__':
    unittest.main()
