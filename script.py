import requests 
import subprocess
import time


url = 'http://votingappg2-testchargeg2.westus.cloudapp.azure.com'
response = requests.head(url)
print(response.headers)
var = 0
Headersss = response.headers
while var < 70:              
    bashcommand="curl -iF 'vote=Dogs' http://votingappg2-testchargeg2.westus.cloudapp.azure.com"
    process = subprocess.run(bashcommand, shell=True, stderr=None, stdout=None)
    time.sleep(1)
    bashcommand2="curl -iF 'vote=Cats' http://votingappg2-testchargeg2.westus.cloudapp.azure.com"
    process = subprocess.run(bashcommand2, shell=True, stderr=None, stdout=None)
    time.sleep(2)
    var = var +1
    print(Headersss)  
    if var == 70:
      break

    

