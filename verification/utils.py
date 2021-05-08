import os
from twilio.rest import Client

account_sid = '' #your sid here
auth_token = '' #your token here
client = Client(account_sid, auth_token)

def send_sms(user_code, phone_number):
    message = client.messages.create(
        body= f'Hi! Your user and verification code is {user_code}',
        from_= '', #generate a number from twilio trial account
        to = f'{phone_number}'

    )

    print(message.sid)