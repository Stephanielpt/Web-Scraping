from twilio.rest import Client #SMS API Package
import time
from twilio.twiml.messaging_response import MessagingResponse

###TWILIO STUFF
account_sid = "AC3c602a60289e0d8b78c843ab743090e1" #Your Twilio account ID
auth_token = "70a0b92d0cf1d2478dfc5e1c376ed0ec"    #Your secret API Token
 
client = Client(account_sid, auth_token)
gotatext = True
while 1:
    def sms_reply():
        """Respond to incoming calls with a simple text message."""
        # Start our TwiML response
        resp = MessagingResponse()

        # Add a message
        resp.message("The Robots are coming! Head for the hills!")
        print("did u even do anythingggg")
        return str(resp)
    quit()
