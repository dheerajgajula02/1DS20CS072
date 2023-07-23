from fastapi import FastAPI, File, UploadFile

import os, requests, sys, socket
import credentials
import json


def creating_fun():
    url = "http://20.244.56.144/train/register"
    data = {
    "companyName": credentials.COMPANY_NAME,
    "ownerName": credentials.OWNER_NAME,
    "ownerEmail": credentials.OWNER_EMAIL,
    "rollNo": credentials.ROLL_NO,
    "accessCode": credentials.ACCESS_CODE
}
    req = requests.post(url, data = data)
    print(req)
    pass


def auths():
    url="http://20.244.56.144/train/auth"
    data=json.dumps({
    "companyName": "Train Central",
    "clientID": "c04e16e3-2a5b-4436-903b-42e7a6ac04ae",
    "clientSecret": "MmmIJSJYWUaOHkak",
    "ownerName": "Dheeraj",
    "ownerEmail": "dheerajgajula2202@gmail.com",
    "rollNo": "072"
})

    req= requests.post(url, data)
    return req.json()["bearerToken"]
  


# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}



# app.post("")

# creating_fun()
# auths()

url="http://20.244.56.144/train/auth"
data={
"companyName": "Train Central",
"clientID": "c04e16e3-2a5b-4436-903b-42e7a6ac04ae",
"clientSecret": "MmmIJSJYWUaOHkak",
"ownerName": "Dheeraj",
"ownerEmail": "dheerajgajula2202@gmail.com",
"rollNo": "072"
}
new_data = json.dumps(data, indent=4)
print(type(data))
req= requests.post(url, new_data)
print(req.json())