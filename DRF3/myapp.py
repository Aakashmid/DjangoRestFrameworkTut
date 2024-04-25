import requests
import json

URL="http://127.0.0.1:8000/stuapi"

def getdata(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,params=json_data)
    data=r.json()   # response return by function
    print(data)

getdata()