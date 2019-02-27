'''
Created on 27 lut 2019

@author: sbartkowski
'''
import unittest
from com.rest import Rest as R


class Test(unittest.TestCase):


    def testName(self):
        res = R.postContent("Hello")
        print(res)
        
    def testFile(self):
        res = R.uploadFile("f.txt")
        print(res)

    def testFileBig(self):
        res = R.uploadFile("upgrade-error.txt")
        print(res)
        
    def testReset(self):
        R.resetCounter()
        
    def testgetCounter(self):
        val = R.getCounter()
        print(val)
        
    def testCounter(self):
        R.resetCounter()
        R.postContent("Hello")
        R.postContent("Hello")
        R.postContent("Hello")
        val = R.getCounter()
        print(val)
        self.assertEqual(val, "3", "Three expected after reset")

