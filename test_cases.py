#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        def test_sample5 (self):
                        self.assertEqual (200, calc(10,20)) 

        def test_sample6 (self):
                        self.assertEqual (499500, calc(500,999))

        def test_sample7 (self):
                self.assertEqual (-1, calc('10','20'))

        def test_sample8 (self):
                        self.assertEqual (-1, calc(5.5,10.5))

        def test_sample9(self):
                        self.assertEqual (-1, calc('abc','10'))

        def test_sample10(self):
                        self.assertEqual (-1, calc('10.','20'))

        def test_sample11(self):
                        self.assertEqual (-1, calc('1a','0'))

        def test_sample12(self):
                        self.assertEqual (-1, calc(None,10))

        def test_sample13(self):
                        self.assertEqual (-1, calc([1,2],50))

        def test_sample14(self):
                self.assertEqual (-1, calc(0,500))

        def test_sample15(self):
                        self.assertEqual (-1, calc(1000,500))

        def test_sample16(self):
                        self.assertEqual (-1, calc(-1,50))

        def test_sample17(self):
                        self.assertEqual (999, calc(1,999))

        def test_sample18(self):
                        self.assertEqual (999, calc(999,1))
                        
        def test_sample19(self):
                self.assertEqual (1, calc(1,1))


