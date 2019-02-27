# MockRest

Simply solution to mock network traffic as HTTP POST request. Can be easily extended to more HTTP methods.<br><br>
The solution as provided as two Eclipse projects: the server and the client. 
The server part is a simple servlet which accepts file uploading and POST request. The target war file can be deployed to Tomcat container.
The client is Python 3 script.

# Server
Get ready to use *war* file (https://github.com/stanislawbartkowski/MockRest/tree/master/RestMockServer/war) and deploy to Tomcat container.<p>
Server part is ready.

You can also download the whole Eclipse project and extend according to your needs.<br>

*Prerequisite for Eclipse project*<br>

The dependecy is resolved using *iy* Eclipse plugin. Install the plugin beforehand.

# Client
## Prerequisites
* Python 3 (tested with Python 3.6 level)<br>
> yum install python36<br>

* *requests* package
>  yum install python36-pip<br>
> python36 -m pip install requests<br>

## Run test
> cd MockRest/CallRest/test/rest<br>
