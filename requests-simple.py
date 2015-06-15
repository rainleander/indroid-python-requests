from sys import argv
import requests

script, first, second, third = argv

keys = {'key1' : first, 'key2' : second, 'key3' : third}
r = requests.get("http://google.nl/?&num=2&q=", params=keys)

print(r.url)
