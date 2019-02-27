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

