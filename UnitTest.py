from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {1: ('1001', 2), 2: ('10', 1), 3: ('0000', 0)}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        s, output = self.__testCases[1]
        result = self.__obj.minChanges(s = s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        s, output = self.__testCases[2]
        result = self.__obj.minChanges(s = s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case3(self):
        s, output = self.__testCases[3]
        result = self.__obj.minChanges(s = s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()