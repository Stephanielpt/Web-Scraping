from twilio.rest import Client #SMS API Package
import time

###TWILIO STUFF
account_sid = "AC3c602a60289e0d8b78c843ab743090e1" #Your Twilio account ID
auth_token = "70a0b92d0cf1d2478dfc5e1c376ed0ec"    #Your secret API Token
 
client = Client(account_sid, auth_token)
gotatext = True
while 1:
    if gotatext:
       gotatext = True
    if gotatext:
       msg = client.messages.create(to="3528704348", from_="3524152946", body="Update! Here you go:http://highbrow.com") #Will send SMS to your phone number
       print ("SMS Sent Thanks")
       
       time.sleep(20) #sleep for 20sec : 2 hours
       gotatext = False
