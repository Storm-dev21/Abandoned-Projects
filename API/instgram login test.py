import requests
import secrets

def generate_csrf_token():
    csrf_token = secrets.token_urlsafe(32)
    return csrf_token

csrf_token = generate_csrf_token()
print("CSRF Token:", csrf_token)

print("Started!")

username = ''
password = ''

URL = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'

headers = {
    'X-CSRFToken': csrf_token,
    'User-Agent': 'Mozilla/5.0',
}

payload = {
    'enc_password': str(password),
    'username': str(username),
}

send = requests.post(URL, data=payload, headers=headers)

if send.status_code == 200:
    response_data = send.json() 
    if 'authenticated' in response_data and response_data['authenticated']:
        print("Login successful")
    else:
        print("Login failed:", response_data.get('message'))
else:
    print("Failed to send message. Response code:", send.status_code)
