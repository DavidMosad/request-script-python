import json
import requests 
import time

data = {
    'vote': 'dogs'
}
url = 'http://votingappg2-testchargeg2.westus.cloudapp.azure.com'

response = requests.post(url,data=data)
print(response.headers)
print(response.status_code)
print(response.headers['X-HANDLED-BY'])
date = response.headers['Date']
time.mktime(date)





