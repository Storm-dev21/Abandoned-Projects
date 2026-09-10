import requests
import time
import os
def continue_():
    from sessions import data1
    while 1==1:
        message_content = input("message:> ")  
        if message_content == 'exit':
            print("quit!")
            quit()

        send_message_url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
        payload = {
            'content': message}
        headers = {
            'Authorization': Token1
        }    
        if token =='':
            print("[!] ERROR!",'Forget the Token? [!]')
        else:
            pass    
        if Channel_ID1 =='':
            print("[!] ERROR!",'Forget the Channel ID? [!]')
        else:
            pass
        if message_content =='':
            print("[!] ERROR!",'Forget the Message? [!]')
        else:
            pass
        response = requests.post(send_message_url, json=payload, headers=headers)
        if response.status_code == 200:
                print(' [ ! ] Sent!')
                message_id = response.json()['id']
                delete_message_url = f'https://discord.com/api/v9/channels/{Channel_ID1}/messages/{message_id}'
                response_delete = requests.delete(delete_message_url, headers=headers)
                if response_delete.status_code == 204:
                    print(" [ * ] DELETED!")
                else:  
                    def error1():   
                        print('ERROR!'+response_delete.text)
                    error1()
        else: 
                def error2():   
                    print("ERROR!"+response.text)
                error2()


def START(Token,Channel_ID,message):
    from config import Token,Channel_ID

    send_message_url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    payload = {
        'content': message}
    headers = {
        'Authorization': Token
    }    
    if token =='':
        print("[!] ERROR!",'Forget the Token? [!]')
    else:
        pass    

    if Channel_ID =='':
        print("[!] ERROR!",'Forget the Channel ID? [!]')
    else:
        pass
    if message =='':
        print("[!] ERROR!",'Forget the Message? [!]')
    else:
        pass
    response = requests.post(send_message_url, json=payload, headers=headers)
    if response.status_code == 200:
            print(' [ ! ] Sent!')
            f = open("sessions.py", "w")
            f.write('''def data1():\n\tglobal Token1,Channel_ID1\n\tToken1=\''''+Token+'''\'\n\tChannel_ID1 =\''''+Channel_ID+'''\'''')
            f.close()
            f = open("config.py", "r")
            print(f.read())
            print("session Created!!")
            message_id = response.json()['id']
            delete_message_url = f'https://discord.com/api/v9/channels/{Channel_ID}/messages/{message_id}'
            response_delete = requests.delete(delete_message_url, headers=headers)
            if response_delete.status_code == 204:
                print(" [ * ] DELETED!")
                continue_()
            else:  
                def error1():   
                    print('ERROR!'+response_delete.text)
                error1()
    else: 
            def error2():   
                print("ERROR!"+response.text)
            error2()

def start(token,channel_id,message):
    from config import Token,Channel_ID
    message = input("message :> ")
    message = str(message)

    send_message_url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    payload = {
        'content': message}
    headers = {
        'Authorization': Token}    
    if token =='':
        print("[!] ERROR!",'Forget the Token? [!]')
    else:
        pass
    if Channel_ID =='':
        print("[!] ERROR!",'Forget the Channel ID? [!]')
    else:
        pass
    if message =='':
        print("[!] ERROR!",'Forget the Message? [!]')
    else:
        pass
    response = requests.post(send_message_url, json=payload, headers=headers)
    if response.status_code == 200:
            print(' [ ! ] Sent!')
            #f = open("sessions.py", "w")
            #f.write('''def data1():\n\tglobal Token1,Channel_ID1\n\tToken1=\''''+Token+'''\'\n\tChannel_ID1 =\''''+Channel_ID+'''\'''')
            #f.close()
            #f = open("config.py", "r")
            #print(f.read())
            #print("session Created!!")
            message_id = response.json()['id']
            delete_message_url = f'https://discord.com/api/v9/channels/{Channel_ID}/messages/{message_id}'
            response_delete = requests.delete(delete_message_url, headers=headers)
            if response_delete.status_code == 204:
                print(" [ * ] DELETED!")
                continue_()
            else:
                def error1():   
                    print('ERROR!'+response_delete.text)
                error1()
    else: 
            def error2():   
                print("ERROR!"+response.text)
            error2()

while True: 
    
    usr=input(" :>")
    if usr=="help"or usr=="-help"or usr=="-h":
        print("--set config\n--new session\n--start session")

    elif usr=="--set config":
        while 1==1:
            token = str(input("Token :>"))
            channel_id =str(input("channel ID :>"))
            if token == '' or token==" ":
                print("Error! Forget the token?")
                continue
            else: channel_id == '' or channel_id == " "
            print("Error! Forget the channel ID?")
            continue


    else:
        print("(!)Error, unknown command!")
        continue





    if usr =='--start' or usr=='start':
        print(f"User token : "+{token}+'\nChannel ID : '+{channel_id})
        f = open("config.py", "w")
        f.write("Token=\'"+token+"\'\n"+"Channel_ID =\'"+channel_id+"\'")
        f.close()
        f = open("config.py", "r")
        print(f.read())
        print("saved!")
        start(token,channel_id)
    #message = input('Message Content :> ')
    #message = str(message)

    #f = open("config.py", "w")
    #f.write("Token=\'"+token+"\'\n"+"Channel_ID =\'"+channel_id+"\'")
    #f.close()
    #f = open("config.py", "r")
    #print(f.read())
    #print("saved!")

    #START(token,channel_id)

#الاخطاء#
# التعامل مع الايرور هاندلغ سيء 
# لا توجد اي الوان او شكل جميل لها 
# لا يستطيع حفظ العناوين و يقترح جعله يحفظ التوكين بل ضبط 
# لا تحتوي على اي خصائص من الأوتوميت

#  # الاضافات حاليا
#امكانية حفظ توكين معين و تغييره متى ما تشاء 
# امكانية حفظ شانيل معينة 

# commands 
# --set config تستعمل لتحديد التوكين و حفظه
# --set Session تستعمل لتحديد توكين و قناة معينة 
