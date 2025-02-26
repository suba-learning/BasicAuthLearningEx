import json

import requests
# https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28

baseurl = "https://api.github.com/user"
username = "@suba-learning"
token = "xxxxx"


#Get userinfo without the token
response = requests.get(baseurl)
print("Status: ",response.status_code)
print(response.json())

#Get User info
response = requests.get(baseurl, auth=(username,token))
print("Status: ",response.status_code)
print(response.json())

#Get User info with incorrect authkey
response = requests.get(baseurl, auth=(username,"xxxx"))
print("Status: ",response.status_code)
print(response.json())

#Get Username
response = requests.get(baseurl, auth=(username,token))
print("Status: ",response.status_code)
print("User Name: ",response.json()["login"])

#Get repos of user
response = requests.get(baseurl+"/repos", auth=(username,token))
print("Status: ",response.status_code)
print(response.json())

#Get repos of user
response =  requests.get("https://api.github.com/users/suba-learning/repos", auth=(username,token))
print("Status: ",response.status_code)
print(response.json())

#Create a repo
payload = {
    "name":"Hello-World",
    "description":"This is first repo created via python Api requests!",
    "private":False
}
headers= {
    "Accept":"application/vnd.github+json"
}
response = requests.post(baseurl, auth=(username,token), data=json.dumps(payload))
print("Status: ",response.status_code)
print(response.json())