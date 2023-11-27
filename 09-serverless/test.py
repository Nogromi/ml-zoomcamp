import requests

# url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
# url = 'https://ihib0zkzd8.execute-api.us-east-1.amazonaws.com/test/predict'
url = 'https://ooo1tk20gi.execute-api.us-east-1.amazonaws.com/test/predict'

data = {'url': 'https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg'}

result = requests.post(url, json=data).json()
print(result)
