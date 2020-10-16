import unittest




class test_in_set_true(unittest.TestCase):
    def test_one(self):
        self.assertTrue(9)

    def test_two(self):
        self.assertFalse(0)


if __name__ == '__main__':
    unittest.main()
