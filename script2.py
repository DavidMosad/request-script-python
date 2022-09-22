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
<<<<<<< HEAD
xhandled = response.headers['X-HANDLED-BY']
# Data to be written
dictionary = {
    xhandled : timestamp
}
 
# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
with open("sample.json", "x") as outfile:
    outfile.write(json_object)
=======




>>>>>>> ca96fe609bef77f65bfb8915e91f6ae6caa9401e

# data2 = {['X-HANDLED-BY']}
#with open("myfile.json", "w") as j:
#	json.dump(data2, j)