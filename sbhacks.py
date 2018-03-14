


from bs4 import BeautifulSoup
from twilio.rest import Client #SMS API Package
import requests

url = "http://highbrow.com/"
# pretend to be a chrome 47 browser on a windows 10 machine
#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
#req = urlRequest.Request(url, headers = headers)

r = requests.get(url)

r = requests.get(url, params=dict(
    query="camila cabello",
    page=2
))

# get the source code
allTheHTML = BeautifulSoup(r, 'html.parser')
##sourceCode = x.read()
s = allTheHTML.find('tr', attrs={'class': '35354 secondline odd'})
hi = s.text.strip()
hi = hi.encode("utf-8")

print (hi)
