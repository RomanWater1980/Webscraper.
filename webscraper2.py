import bs4
import requests
import time
o = input("What is the link?\n")
res = requests.get(o)
print(res.text)
time.sleep(1000000)
