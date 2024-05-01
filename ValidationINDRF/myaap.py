# python application for using api we create
import json
import requests

url='http://127.0.0.1:8000/stucreate/'

data={
    'name':'Ayan',
    'roll':56,
    'city':'Delhi'
}
json_data=json.dumps(data)
r=requests.post(url=url,data=json_data)
data=r.json()
print(data)