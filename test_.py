import unittest
from q3 import *
from q5 import *
from q7 import *
class Test(unittest.TestCase):
    def test_check_duplicate(self):
        self.assertAlmostEqual(remove_duplicate([12,24,35,24,88,120,155,88,120,155]),[12, 24, 35, 88, 120, 155])
        
    def test_binary_search_value(self):        
        self.assertEqual(binary_Search([1,23,56,89,78,87],23),1)
    
    def test_split_string(self):
        self.assertAlmostEqual(split_string(),"companyname")
  
if __name__ == '__main__':
    unittest.main()