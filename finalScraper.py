import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from twilio.rest import Client #SMS API Package
import re
import time

req = urllib.request.Request('https://stephanielpt.github.io/', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
# specify the url
hbpage = 'http://www.hm.com/us'

# query the website and return the html to the variable ‘page’
page = urlopen(hbpage)

# parse the html using beautiful soap and store in variable `soup`
allTheHTML = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
name_box = allTheHTML.find('div', attrs={'class': 'teaser-headline'})
name = name_box.text.strip() # strip() is used to remove starting and trailing
print (name)

###compareTo = name;

###TWILIO STUFF
account_sid = "AC3c602a60289e0d8b78c843ab743090e1" #Your Twilio account ID
auth_token = "70a0b92d0cf1d2478dfc5e1c376ed0ec"    #Your secret API Token
 
client = Client(account_sid, auth_token)
 
while 1:

    if name != "Wear Essie Geranium on Your Nails For The Rest of SummerEndorsed by Olivia Palermo, verified by our writers.In The KnowBy Team HighbrowJuly 5, 2017": 
       msg = client.messages.create(to="3528704348", from_="3525058303", body="Update! Here you go:http://highbrow.com") #Will send SMS to your phone number
       print ("SMS Sent Thanks")
       quit()
 
    else:
       
       print ("Nothing here. Going to sleep") #will not send anything
       time.sleep(7200) #sleep for 2 hours

