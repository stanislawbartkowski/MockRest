'''
Created on 27 lut 2019

@author: sbartkowski
'''

import requests
import os
from pathlib import Path

#SERVERHOST="localhost"
SERVERHOST="streams43.sb.com"
APPNAME="RestMockServer"

class RestError(Exception): 
  
    # Constructor or Initializer 
    def __init__(self, err,errmess):
        self.err = err 
        self.errmess =  errmess
  
    # __str__ is to print() the value 
    def __str__(self): 
        return(self.err + " " + self.errmess) 


def __getRestURL(rest="rest"):
    if rest : return "http://"+ SERVERHOST + ":8080/" + APPNAME + "/rest"
    return "http://"+ SERVERHOST + ":8080/" + APPNAME

def __getText(r):
    if r.status_code == 204 : return ""
    if r.status_code != 200 : raise(RestError("Error while reading REST data",str(r.content)))
    return r.text

def __getRest(url):
    r = requests.get(url)
    return __getText(r)

def __postContent(rest,content):
    url = __getRestURL() + "/" + rest + "?content=" + content
    r = requests.post(url)
    return __getText(r)

def postContent(content):
    return __postContent("postform", content)

def uploadFile(filename) :
    c = os.path.dirname(os.path.abspath(__file__))
    fname = os.path.join(c,"../../resource/",filename)
    files = { 'file' : open(fname,'r')}
    url = __getRestURL(None) + "/upload"
    r = requests.post(url,files=files)
    return __getText(r)

