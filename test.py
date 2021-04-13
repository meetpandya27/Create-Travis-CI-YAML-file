from volume import *
import unittest

class TestCuboid (unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(volume(2),8)
        self.assertAlmostEqual(volume(1),1)
        self.assertAlmostEqual(volume(0),0)
        self.assertAlmostEqual(volume(5.5),166.375)
