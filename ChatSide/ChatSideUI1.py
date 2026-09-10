import pyautogui
from customtkinter import *

#Body Program structure#
root=CTk      (             )
root.geometry ("800x590"    )
root.config   (bg="black"   )
root.title    ('ChatSide_V1')
root.resizable(0,0          )
root.iconbitmap(            )
#MainBodyFrame#
Mframe = CTkFrame(root,width=780,height=580,
                  bg_color='black',border_width=13,
                  corner_radius=20,border_color='#FFD800',
                  fg_color="black").place(x=10,y=5)
#var        type     master  text           text color             bg color          font                       place-pack #                      
LogoLabel = CTkLabel(Mframe,text='ChatSide',text_color='#FFD800',bg_color='black',font=('Cascadia Code',25,))    .place(x=350,y=20)
logolabel = CTkLabel(Mframe,text='Discord auto\nmessage sender',
                                           text_color='#FFD800',bg_color='black',font=('Cascadia Code',12,'bold')).place(x=360,y=50)
# - Chat members Functions and body - # =================================
# var type      master  height     width     backGround co   foreGround co    cornerR          BorderColor             Border Width                         
FC  = CTkFrame(Mframe,height=394,width=344,bg_color="black",fg_color='black',corner_radius=12,border_color="#FFD800",border_width=1)         .place(x=30 ,y=90 ) #mainFrame
LAB = CTkLabel(Mframe,text="Chat Members" ,bg_color="black",text_color="#FFD800",font=('Cascadia Code',13,'bold'))                           .place(x=50 ,y=100) #Chatmembers text
LAB2= CTkLabel(Mframe,text="Person one" ,bg_color="black",text_color="#FFD800",font=('Cascadia Code',11,'bold'  ))                           .place(x=75 ,y=120) #person one
LAB3= CTkLabel(Mframe,text="Person two" ,bg_color="black",text_color="#FFD800",font=('Cascadia Code',11,'bold'  ))                           .place(x=250,y=120) #person two

# - save Button (Chat members Function)
F     = CTkFrame (FC,height=84,width=335,bg_color="black",fg_color="black",corner_radius=12,border_color="#FFD800",border_width=1)          .place(x=35 ,y=395)
Button= CTkButton(F,height=35,width=20,text="Save",text_color="#FFD800",bg_color="black",font=('Cascadia Code',9,'bold'),fg_color="black",corner_radius=12,border_color="#FFD800",border_width=2,hover_color="white").place(x=320 ,y=420)
LAB4= CTkLabel(F,text="its automation tool\n makesure to make person 1 and 2 are \nfrom the left side and right side in ur window" ,bg_color="black",text_color="#FFD800",font=('Cascadia Code',10))      .place(x=40 ,y=410) #label info

# ========================================================================

root.mainloop()