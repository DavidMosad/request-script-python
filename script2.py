import json
import requests 
import time
import datetime

data = {
    'vote': 'dogs'
}
url = 'http://votingappg2-testchargeg2.westus.cloudapp.azure.com'

response = requests.post(url,data=data)
print(response.headers)
print(response.status_code)
print(response.headers['X-HANDLED-BY'])
date = response.headers['Date']
timestamp = time.mktime(datetime.datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT").timetuple())





