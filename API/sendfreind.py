import requests

print("Started!")

token = 'MTExNzU2MjU2MjI0Mjk0NTA2NQ.GF4u9i.zt8GmX-NFEuk7dW6gmXuHG8RU6Qo1OqtaWfC64'
useID = '700398313005908079'

URL = f'https://discord.com/api/v9/users/@me/relationships/{useID}'

headers = {
    'Authorization': token}

send = requests.put(URL,headers=headers)

if send.status_code == 200:
    print("Message sent successfully")
else:
    print("Failed to send message:", send.text)