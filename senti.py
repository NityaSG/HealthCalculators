import requests
 
def send_sms(api_key, sender, numbers, message):
    url = 'https://api.textlocal.in/send/'
    data = {
        'apikey': api_key,
        'numbers': numbers,
        'message': message,
        'sender': sender
    }
 
    response = requests.post(url, data=data)
    response_data = response.json()
 
    if response_data['status'] == 'success':
        print('SMS sent successfully.')
    else:
        print('Error occurred while sending SMS.')
        print('Error message:', response_data['errors'][0])
 
# Set your Textlocal API credentials
API_KEY = 'NTE2OTY2Mzk3ODUzNzU3NDUzNjI0YTU0MzQ2NjUyNDc='
SENDER = 'Ashish AVS'
 
# Set the phone numbers and message
PHONE_NUMBERS = '917997707752'
MESSAGE = 'Hello, this is a test message.'
 
# Send SMS
send_sms(API_KEY, SENDER, PHONE_NUMBERS, MESSAGE)