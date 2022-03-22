import urllib.request
import requests
import os

query = "manatee"
amount = 150
secret_key = ''

url = "https://api.bing.microsoft.com/v7.0/images/search?q=" + \
    query+"&count="+str(amount)+"&offset=0"
headers = {'Accept': '*/*', 'User-Agent': 'python',
           'Ocp-Apim-Subscription-Key': secret_key}
response = requests.get(url, headers=headers)
responseJSON = response.json()
responseValues = responseJSON["value"]

i = 0

os.mkdir(query)

for value in responseValues:
    print("Downloading from " + value["contentUrl"])
    try:
        urllib.request.urlretrieve(
            value["contentUrl"], query+"/"+query+"-"+str(i)+"."+value["encodingFormat"])
        i = i+1
    except:
        print("Failed to download")
