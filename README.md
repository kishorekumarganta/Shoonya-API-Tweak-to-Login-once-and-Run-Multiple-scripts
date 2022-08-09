# Shoonya API Tweak to Login once and Run Multiple scripts
# I am single, Unable to fetch Time Here, So Taking too Much Time for every release.

# When you run two Scripts Parallely in Shoonya, One i.e old One is killed by some error.
# Here we tweaked the Issue and Succesfully enabled shoonya API to run Multiple Scripts.

# For That we store the access token that we generate on login and store it in a text file
# and every time we use that access token every time we run a script,we wont need to Login Every Time.
# this allows us to run Multiple Scripts.

****
Refer Below for Login Basics and Initial Setup 

github Link:
https://github.com/kishorekumarganta/How-to-setup-Finvasia-Shoonya-Api-Login-and-Generate-Session
****

****
Firstly we need to get the NorenAPI.py file from the C Drive

NorenApi.py Path in C Drive to Get:
C:\Users\gkk_I\AppData\Local\Programs\Python\Python310\Lib\site-packages\NorenRestApiPy

****

We Used API_Helper.py to Tweak NORENAPI

Open API_Helper.py

Try to Find  Below Code in API_Helper.py file

```
class ShoonyaApiPy(NorenApi):
    def __init__(self):
        NorenApi.__init__(self, host='https://shoonyatrade.finvasia.com/NorenWClientTP/', websocket='wss://shoonyatrade.finvasia.com/NorenWSTP/', eodhost='https://shoonya.finvasia.com/chartApi/getdata/')
        global api
        api = self

```

Copy The Below from API_Helper.py
host='https://shoonyatrade.finvasia.com/NorenWClientTP/', 
websocket='wss://shoonyatrade.finvasia.com/NorenWSTP/', 
eodhost='https://shoonya.finvasia.com/chartApi/getdata/'

****
Try to Find  Below Code in NorenApi.py file

```
    def __init__(self, host, websocket, eodhost):
        self.__service_config['host'] = host
        self.__service_config['websocket_endpoint'] = websocket
        self.__service_config['eoddata_endpoint'] = eodhost

```

Replace Code in NorenApi.py file with copied data from API_Helper.py

```
    def __init__(self):
        self.__service_config['host'] = 'https://shoonyatrade.finvasia.com/NorenWClientTP/'
        self.__service_config['websocket_endpoint'] = 'wss://shoonyatrade.finvasia.com/NorenWSTP/'
        self.__service_config['eoddata_endpoint'] = 'https://shoonya.finvasia.com/chartApi/getdata/'

```

Try to Find  Below Code in NorenApi.py file

```
   self.__username   = userid
        self.__accountid  = userid
        self.__password   = password
        self.__susertoken = resDict['susertoken']

```

Below it in the same Indentation Write below Code:

```
   self.__username   = userid
        self.__accountid  = userid
        self.__password   = password
        self.__susertoken = resDict['susertoken']
        #our Additional Code Follows here
        #Here, we are Storing the Super token we got in shoonyakey.txt file
        f=open("shoonyakey.txt",'w')
        f.write(resDict['susertoken'])
        f.close()

```
****

Try to Find Below Code

```
        self.__username   = userid
        self.__accountid  = userid
        self.__password   = password
        self.__susertoken = resDict['susertoken']
        #reportmsg(self.__susertoken)
        #our Additional Code Follows here
        #Here, we are Storing the Super token we got in shoonyakey.txt file
        f=open("shoonyakey.txt",'w')
        f.write(resDict['susertoken'])
        f.close()

        return resDict
```

Also at start 
```import config```

After the above code, we have to define a function token_setter()

```
    def token_setter(self):
        token=open("shoonyakey.txt",'r').read().rstrip()
        self.__susertoken=token
        #after login we set our token directly,so we also to define our username and password
        self.__username=config.user
        self.__password=config.pwd
        self.__accountid=config.user
```

****
## Now Create an Test Py File ==> login.py

```
from NorenApi import NorenApi
import config
shoonya=NorenApi()
#We set the Object

shoonya.login(config.user,config.pwd,config.factor2,config.vc,config.app_key,config.imei)
#check Config FIle for whether we defined these there are not with same names

# from NorenApi
#def login(self, userid, password, twoFA, vendor_code, api_secret, imei):

#REmember to define the Credentials same like Above in Config File.

```

once we run above File we will get shoonyakey.txt file auto generated and has written the code auto inside it i.e token

****
## Now Create an Test Py File ==> test2itc.py
Must Enter in NorenAPI FIle your Username and Password Directly






## Now Create an Test Py File ==> test3reliance.py



## Author

Ganta Kishore Kumar

****

## License

Copyright (C) of API belong to API Owners.

****
