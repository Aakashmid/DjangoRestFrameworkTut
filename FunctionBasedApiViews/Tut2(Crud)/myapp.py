import requests
import json

URL="http://127.0.0.1:8000/studentapi/"

def getdata(id=None):
    data={}
    if id is not None:
        data={'id':id}
    headers={"content-Type":"application/json"}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data,headers=headers)
    data=r.json()   # response return by function
    print(data)

def postdata():
    data={'name':'Steve','roll_no':6,'city':'New York'}
    json_data=json.dumps(data)
    headers={"content-Type":"application/json"}
    r=requests.post(url=URL,data=json_data,headers=headers)
    data=r.json()   # response return by function
    print(data)

def updatedata():
    data={'id':2,'name':'Steve Rogers'} # partial update
    # data={'name':'Steve','roll_no':6,'city':'New York'} # complete update
    json_data=json.dumps(data)
    headers={"content-Type":"application/json"}
    r=requests.put(url=URL,data=json_data,headers=headers)
    data=r.json()   # response return by api
    print(data)


def deletedata():
    data={'id':1}
    json_data=json.dumps(data) # convert python data to json data
    headers={"content-Type":"application/json"}
    r=requests.delete(url=URL,data=json_data,headers=headers)
    data=r.json()
    print(data)

# getdata(1)
# getdata()
# postdata() # for creating data
# updatedata() #for updating
deletedata()