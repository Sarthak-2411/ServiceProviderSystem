from .otp_generator import generate_otp
from twilio.rest import Client

account_sid = 'AC6438f5e6a4a732057f040379e7d7a5b1'
account_token = 'de4d21512da58beec66ff0dc7e5f5f64'
client = Client(account_sid, account_token)

def send_otp(number: str):
    try: 
        otp = generate_otp()
        message = otp + "  is your OTP for Home Service Login"
        # number = '+91'+number
        # Uncomment below line when sending actual OTP
        # client.messages.create(from_= '+14155349508',body = message,to = number) # eg. number = '+919403051370'

        print(message)
        return otp
    except:
        return None
