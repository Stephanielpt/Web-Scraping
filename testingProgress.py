
from urllib.request import urlopen
from bs4 import BeautifulSoup
from twilio.rest import Client #SMS API Package
import re
import time
import urllib.request as urlRequest
import urllib.parse as urlParse

url = "http://highbrow.com/"
# pretend to be a chrome 47 browser on a windows 10 machine
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
req = urlRequest.Request(url, headers = headers)
# open the url
x = urlRequest.urlopen(req)
# get the source code
allTheHTML = BeautifulSoup(x, 'html.parser')
##sourceCode = x.read()
name_box = allTheHTML.find('article', attrs={'class': 'c4-4 story n1'})
name = name_box.text.strip()
name = name.encode("utf-8")
print (name)

###compareTo = name;

###TWILIO STUFF
account_sid = "AC3c602a60289e0d8b78c843ab743090e1" #Your Twilio account ID
auth_token = "70a0b92d0cf1d2478dfc5e1c376ed0ec"    #Your secret API Token
 
client = Client(account_sid, auth_token)
 
while 1:

    if name != b'Wear Essie Geranium on Your Nails For The Rest of SummerEndorsed by Olivia Palermo, verified by our writers.\nIn The KnowBy Team HighbrowJuly 5, 2017': 
       msg = client.messages.create(to="3528704348", from_="3525058303", body="Update! Here you go:http://highbrow.com") #Will send SMS to your phone number
       print ("SMS Sent Thanks")
       quit()
 
    else:
       
       print ("Nothing here. Going to sleep") #will not send anything
       time.sleep(7200) #sleep for 2 hours

