import requests


print("Started!")

# Credentials
username = 'a1944176@gmail.com'
password = ''

URL = 'http://192.168.0.1/cgi?2' #enable

# Set headers
headers = {
    'target''0C:FE:45:ED:3C:23'
}

# Set payload
payload = {
    '[RULE#16,0,0,0,0,0#0,0,0,0,0,0]0,1',
    'enable'=='0'
}

# Send POST request
send = requests.post(URL, payload, headers=headers)