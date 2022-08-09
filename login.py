from NorenApi import NorenApi
import config
shoonya=NorenApi()
#We set the Object


#General Login with out Token ,Cant run Multiscript Here,
#Try to Check other two Examples Uploaded here.
shoonya.login(config.user,config.pwd,config.factor2,config.vc,config.app_key,config.imei)

# from NorenApi
#def login(self, userid, password, twoFA, vendor_code, api_secret, imei):

#REmember to define the Credentials same like Above in Config File.