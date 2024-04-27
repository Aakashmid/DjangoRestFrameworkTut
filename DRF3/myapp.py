import requests
import json

URL="http://127.0.0.1:8000/stuapi/"

def getdata(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,params=json_data)
    data=r.json()   # response return by function
    print(data)

def postdata():
    data={'name':'Steve','roll_no':6,'city':'New York'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()   # response return by function
    print(data)

def updatedata():
    data={'id':5,'name':'Steve','roll_no':10,'city':'Berlin'} # partial update
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()   # response return by api
    print(data)


def deletedata():
    data={'id':6}
    json_data=json.dumps(data) # convert python data to json data
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)

# getdata()
# postdata() # for creating data
# updatedata() #for updating
deletedata()