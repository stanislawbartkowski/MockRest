'''
Created on 27 lut 2019

@author: sbartkowski
'''

from com.rest import Rest
import time
import sys

# __runTest1
# number of iterations
#NO=1000
NO=1000

# __runTest2
# time elapsed
SEC = 5 * 60

#SERVERHOST="thinkde:8080"
#APPNAME="RestMockServer"


class runRest :
    
    def __init__(self,server,app):
        self.start = time.time()
        self.no = 0
        self.R = Rest.RestApi(server,app)
        
    def _printProgress(self):
        end = time.time()
        print("Number of calls:",self.no)
        print("Time elapsed:",(end -self.start))
        print("Calls/sec",self.no / (end-self.start))
        
    def __progress(self):
        if self.no % 500 == 0 :
            self._printProgress()
            print("-------------")
            
        
    def runIter(self):
        for self.no in range(NO) :
            self.restTest()
            self.__progress()
        self.no = NO
        
    def runTime(self):
        while time.time() - self.start < SEC :
            self.restTest()
            self.__progress()
            self.no = self.no + 1
        
    def printResult(self):
        print("=============")
        self._printProgress()
        
    def restTest(self):
        res = self.R.postContent("Hello")

def printHelp() :
    print("Parameters: /what/ /server/ /appname/")
    print(" 1 : number of iterations: ",NO)
    print(" 2 : time elapsed. Number of seconds:",SEC)
    print("Example:")
    print(" MainRun.py 1 localhost:8080 RestMockServer ")
    sys.exit()
    
        
if __name__ == '__main__':
    if len(sys.argv) != 4 : 
        printHelp()
        
    test = sys.argv[1]
    server = sys.argv[2]
    app = sys.argv[3]
    
    if test == "1" :
        r = runRest(server,app)
        r.runIter()
    elif test == "2":
        r = runRest(server,app)
        r.runTime()
    else :
        printHelp()
        
    r.printResult() 
        
        
    
        
