# Webscraper.
Simple Webscaper build in Python. I'm not responsible if you use this to do anything illegal, I also don't advise you to. This is made for legal purposes.
Requires bs4. You can install bs4 by going to the Command Prompt in Windows, as an administatrator(haven't tested pip install on non administrator CMD so for result matching mine use admistrator) type "pip install bs4" without the speech marks.

NOTE: Only webscrapes HTTPS or HTTP. .com does not work. I have not tested any other types, but please put it in issues if you find any other type that doesn't work and I will try and resolve that.

If you want any more features added to this, let me know. 

The source code for this is as follows.

import bs4
import requests
o = input("What is the link?\n")
res = requests.get(o)
print(res.text)
