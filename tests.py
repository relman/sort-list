import unittest
from main import sort_list


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertSequenceEqual(sort_list('1'.split()), '1'.split())

    def test2(self):
        self.assertSequenceEqual(sort_list('car truck bus'.split()), 'bus car truck'.split())

    def test3(self):
        self.assertSequenceEqual(sort_list('8 4 6 1 -2 9 5'.split()), '-2 1 4 5 6 8 9'.split())

    def test4(self):
        self.assertSequenceEqual(sort_list('car truck 8 4 bus 6 1'.split()), 'bus car 1 4 truck 6 8'.split())

    def test5(self):
        self.assertSequenceEqual(sort_list('car truck -8 -88 bus 6 1'.split()), 'bus car -88 -8 truck 1 6'.split())

    def test6(self):
        self.assertSequenceEqual(sort_list('999999 -999999 9 -9 0'.split()), '-999999 -9 0 9 999999'.split())

    def test7(self):
        self.assertSequenceEqual(sort_list('cba cab bca acb abc bac'.split()), 'abc acb bac bca cab cba'.split())


if __name__ == '__main__':
    unittest.main()