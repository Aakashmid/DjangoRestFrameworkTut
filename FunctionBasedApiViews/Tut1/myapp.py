import json
import requests

url='http://127.0.0.1:8000/stuapi/'


def getdata():
    r=requests.get(url=url)
    data=r.json()
    print(data)

def postdata():
    data={
        'name':'Suraj',
        'roll':5,
        'city':'Patna'
    }
    json_data=json.dumps(data)

    headers={'content-Type':'application/json'}
    r=requests.post(url=url,headers=headers,data=json_data)
    data=r.json()
    print(data)

# getdata()
postdata()