def add(a,b):
    return a+b
if __name__=='__main__':
    result=add(5,3)
    print(f"The sum of two numbers is:" ,result)

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
