'''
Created on 27 lut 2019

@author: sbartkowski
'''

from com.rest import Rest as R

NO=1000

def __runRest1() :
    for i in range(NO) :
        res = R.postContent("Hello")
        if i % 100 == 0 : print(i)
#        print(res)
#        print(i)

if __name__ == '__main__':
    __runRest1()