from fastapi import FastAPI, File, UploadFile

import os, requests, sys, socket
import credentials
import json

def token_generation():
    url = "http://20.244.56.144/train/register"
    data = {
    "companyName": credentials.COMPANY_NAME,
    "ownerName": credentials.OWNER_NAME,
    "ownerEmail": credentials.OWNER_EMAIL,
    "rollNo": credentials.ROLL_NO,
    "accessCode": credentials.ACCESS_CODE
}
    new_data = json.dumps(data, indent=4)
    req = requests.post(url, data = new_data)
    return req.json()

def auths():
    url="http://20.244.56.144/train/auth"

    #new_data = token_generation()
    
    data={
    "companyName": "Train Central",
    "clientID": "c04e16e3-2a5b-4436-903b-42e7a6ac04ae",
    "clientSecret": "MmmIJSJYWUaOHkak",
    "ownerName": "Dheeraj",
    "ownerEmail": "dheerajgajula2202@gmail.com",
    "rollNo": "072"
    }
    new_data = json.dumps(data, indent=4)

    req= requests.post(url, new_data)
    return req.json()





import requests

app = FastAPI()

# Assuming you have already registered your company and obtained the access token
access = auths()
print(access)
access_token = access["access_token"]
API_URL = "http://20.244.56.144/train/trains"

@app.get("/trains")
def get_train_schedule():
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(API_URL, headers=headers)
    json_resp = response.json()
    print(json_resp[0])
    return response.json()



