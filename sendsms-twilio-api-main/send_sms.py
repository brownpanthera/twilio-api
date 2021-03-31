'''
Send SMS using Twilio API
'''

from twilio.rest import Client


account_sid = 'Your-SID'
auth_token = 'Your-Token'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="hello! this is a programmed message",
                     from_='number',
                     to='number'
                 )

print(message.sid)

