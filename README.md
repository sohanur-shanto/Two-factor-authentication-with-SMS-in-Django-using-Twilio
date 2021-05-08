# Two-factor-authentication-with-SMS-in-Django-using-Twilio

Hi folks! if you want to use this particular feature to verify your user then follow this steps.
Go to this website [Twilio](https://www.twilio.com/docs/sms),
get sid, auth token and generate a number for trial, they will give you $15 for trial account. feel free to use those credits :P
 1. pip install -r requirements.txt
 2. pip install virtualenv
 3. virtualenv env
 4. .\env\scripts\activate
 5. python manage.py migrate
 6. python manage.py runserver 
 
 Enjoy ! Don't forget to use your token number and sid that you get from twilio. change verification/utils.py this.
