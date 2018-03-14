from twilio.rest import Client #SMS API Package
import time
from twilio.twiml.messaging_response import MessagingResponse

###TWILIO STUFF
account_sid = "" #Your 
auth_token = ""    #Your Token
 
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
