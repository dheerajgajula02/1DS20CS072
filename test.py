import sys,socket

import requests
import credentials

url = "http://20.244.56.144/train/trains"

# headers = {
#     "Authorization":"Bearer "+ credentials.BEARER_TOKEN
# }

data = {
    "companyName": "Train Central",
    "clientID": "c04e16e3-2a5b-4436-903b-42e7a6ac04ae",
    "clientSecret": "MmmIJSJYWUaOHkak",
    "ownerName": "Dheeraj",
    "ownerEmail": "dheerajgajula2202@gmail.com",
    "rollNo": "072"
}


url_2 = "http://20.244.56.144/train/auth"
req = requests.post(url_2, data = data)
print(req)



# r= requests.get(url,headers= headers) 
# print(r.text)