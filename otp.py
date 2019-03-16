import requests
import json
import random

URL = 'http://www.way2sms.com/api/v1/sendCampaign'

ran=random.randint(1000,9999)
# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':'EJNDMSDX8B6M48NCT43L5Q5MXW4SKIH4',
  'secret':'YSXVIV4B6FVW7LLT',
  'usetype':'stage',
  'phone': '7012161270',
  'message':'OTP is 9849' ,
  'senderid':'Rizwan'
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest(URL, 'EJNDMSDX8B6M48NCT43L5Q5MXW4SKIH4', 'YSXVIV4B6FVW7LLT', 'stage', '8089553454', 'Rizwan', 'message-text' )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
and then requst to api
"""
# print response if you want
print (response.text)

