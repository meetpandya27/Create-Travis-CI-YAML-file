from volume import *
import unittest

class Test (unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(volume(0),0)
        self.assertAlmostEqual(volume(1),1)
        self.assertAlmostEqual(volume(3),27)
        self.assertAlmostEqual(volume(10),1000)


if __name__ == '__main__':
    unittest.main()
