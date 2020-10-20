import unittest
from more_fun_with_collections.assign_average import add
from more_fun_with_collections.assign_average import sub
from more_fun_with_collections.assign_average import mul
from more_fun_with_collections.assign_average import div



class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(add(), 4)
        self.assertEqual(sub(), 0)
        self.assertEqual(mul(), 4)
        self.assertEqual(div(), 1)

if __name__ == 'main':
    unittest.main()





if __name__ == '__main__':
    unittest.main()
