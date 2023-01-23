import sys
import unittest
sys.path.append('../src/')
import tools


class GetPixelsTesting(unittest.TestCase):

    def check_not_empty_list(self):
        
        self.assertNotEqual(tools.get_pixels("../examples_digits/1.jpg"), [])
        

if __name__ == '__main__':
    unittest.main()