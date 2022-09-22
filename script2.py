import requests 
import subprocess
import time


url = 'http://votingappg2-testchargeg2.westus.cloudapp.azure.com'
response = requests.post(url,params= "vote=Dogs")
print(response.headers)
print(response.status_code)

    

