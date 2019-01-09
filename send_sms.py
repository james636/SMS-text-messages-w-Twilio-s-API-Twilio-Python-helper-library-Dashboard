# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACdce4223c22e899b93bbea6cdb2fd2ea9'
auth_token = 'b32ccdd6fe1822d37348ed6736473e13'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="I created this program with Python and Twilio API and helper library to text SMS messages.",
                     from_='+16363031034',
                     to= '+1' + input('What number would you like to text, with area code?')
                 )

print(message.sid)
