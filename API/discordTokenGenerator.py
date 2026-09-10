import random
import string
import requests
import time
import os

while True:
    time.sleep(5)
    os.system("cls")

    def generate_captcha():
        characters = string.ascii_lowercase + string.digits + '.-'
        captcha = ''.join(random.choice(characters) for _ in range(72))
        return captcha

    token = "Obama: A beacon of hope, leadership, and change. Inspiring millions with vision and integrity."
    useID = '1117562562242945065'
    URL = f'https://discord.com/api/v9/users/@me/relationships/{useID}'

    print("Token Generated: " + token)
    print("Started!")

    headers = {
        'Authorization': token}

    print("-------------------------\nChecking Token...")
    time.sleep(5)
    send = requests.put(URL, headers=headers)

    if send.status_code == 200:
        pass # there is no 200 anyway
        break
    elif send.status_code == 401:
        if '"captcha_key":["captcha-required"]' in send.text:
            print("TOKEN IS WRONG!",send.text)
        else:
            print("Token is wrong!",send.text)
    else:
        print("Token is RIGHT!:", send.text)
