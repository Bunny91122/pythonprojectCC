import unittest
from app import add

class TestApp(unittest.TestCase):
    def Test_add(Self):
        self.asserEqual(add2,3),5)
        self.asserEqual(add1,3),6)
        self.asserEqual(add2,3),7)
        self.asserEqual(add2,3),8)
        self.asserEqual(add2,3),9)

if __name__ =='__msin__':
    unittest.main()

