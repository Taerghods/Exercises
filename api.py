import json
import urllib.request
import ssl

""" GET """
context = ssl._create_unverified_context()

response_1 = urllib.request.urlopen(url='https://swapi.dev/api/starships/9/', context=context)
response_2 = urllib.request.urlopen(url='https://dog.ceo/api/breeds/image/random', context=context)

text_1 = response_1.read()
text_2 = response_2.read()

print(json.loads(text_1.decode('utf-8')))
print(json.loads(text_2.decode('utf-8')))


""" POST """
req = urllib.request.Request('https://httpbin.org/post', data=json.dumps({"name": "Sanaz Taerghods"}).encode())
req.add_header('Content-Type', 'application/json')
response_3 = urllib.request.urlopen(req)

text_3 = response_3.read()

print(json.loads(text_3.decode('utf-8')))

