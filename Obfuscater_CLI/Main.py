import requests
import time
import os
import pyperclip

def start():
    while True:
        try:
            
            for i in range(10):
                global times1,script,lang
                print("depends on how big is your code(cant encode a 400 lines of code more than 3 times)\n")
                times1 = int(input('how many times u want it to encode :> '))
                script = input('Code:> ').upper()
                lang = input('Lang:> ').upper()
                if script == 'EXIT' or lang == 'EXIT':
                    print(" [!] QUIT! [!] ")
                    quit()
                elif times1 > 250:
                    print("Too many REQUESTS!")
                    times1 = 200
                elif script == '':
                    print('[ ! ] Error! Please insert a command! [ ! ]')
                    continue
                elif lang =='':
                    print(' [ ! ] ERROR!,Please insert a language! [ ! ] ')
                    continue
                else:
                    pass    
                request()
            print("Delay ..API will Block ur ip if u keep sending too much requests \nPlease wait..")
            time.sleep(4)
            os.system('cls')
        except ValueError:
            print(f' [ ! ] Error [ ! ] ValueError: invalid literal for int() with base 10 ')
            continue
        except Exception as e2:
            print(' [ ! ] Error! :'+str(e2)+' [ ! ] ')
            continue
        except KeyboardInterrupt:
            print("[ ! ] Exit [ ! ]")
            quit()
def timer():
        duration = 10
        start_time = time.time()
        while True:
            os.system('cls')
            elapsed = time.time() - start_time
            print(f' [ + ] Please wait 10s({int(elapsed)}) [ + ] ')
            time.sleep(1)
            if elapsed >= duration:
                break
        print("\nDone!")
def request():  
        
        global times1
        for x in range(times1):  
            times1 -=1
            if times1 < 15:
                url = 'https://freecodingtools.org/api/obfuscator'
                payload = {'code': script, 'language': lang}
                res = requests.post(url, json=payload)
                time.sleep(2)
            if res.status_code == 200:
                text = res.text 
                if times1 ==0:
                    pyperclip.copy(text[44:])
                    print("[ * ] DONE! , Code Copied to the ClipBoard! [ * ]")
                else:
                    continue
            else:
                print("[ ! ] Error! [ ! ]")


        else:
            print("[ * ] Done! [ * ]")

start()
timer()