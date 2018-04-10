
#####import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from twilio.rest import Client #SMS API Package
import re
import time
import urllib.request as urlRequest
import urllib.parse as urlParse
#####from http.cookiejar import CookieJar

url = "http://classes.usc.edu/term-20183/classes/thtr"
# pretend to be a chrome 47 browser on a windows 10 machine
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
req = urlRequest.Request(url, headers = headers)
# open the url
#####cj = CookieJar()
#####opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#####x = opener.open(req)

x = urlRequest.urlopen(req)

# get the source code
allTheHTML = BeautifulSoup(x, 'html.parser')
##sourceCode = x.read()
name_box = allTheHTML.find('tr', attrs={'class': '62633 even'})
name = name_box.text.strip()
name = name.encode("utf-8")
print (name)

###TWILIO STUFF
account_sid = "AC3c602a60289e0d8b78c843ab743090e1" #Your Twilio account ID
auth_token = "70a0b92d0cf1d2478dfc5e1c376ed0ec"    #Your secret API Token
 
client = Client(account_sid, auth_token)
 
while 1:
    newX = urlRequest.urlopen(req)
    newAllTheHTML = BeautifulSoup(newX, 'html.parser')
    new_name_box = newAllTheHTML.find('tr', attrs={'class': '62633 even'})
    newName = new_name_box.text.strip()
    newName = newName.encode("utf-8")
    print (newName)
    if newName != name: 
       msg = client.messages.create(to="3528704348", from_="3525058303", body="IT'S UP! IT'S UP!!! IT IS OPENNNN") #Will send SMS to your phone number
       print ("SMS Sent Thanks")
       name = newName
       quit()
 
    else:
       
       print ("Nothing here. Going to sleep for a couple hours") #will not send anything
       time.sleep(10) #sleep for 2 hours
       
###You know how to change this:
###Have old name --> grab a new name and check against in every while loop
###If same: sleep, if different send text and set old to the current new
###Authenitfication for users on balckboard - check grades

