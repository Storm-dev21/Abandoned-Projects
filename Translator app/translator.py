from customtkinter import *
from tkinter import *
from PIL import Image
from googletrans import Translator, LANGUAGES

# Main colors
bg = '#135eaa'
fg = '#e2effc'
# Frame colors
txt = '#368fe9'
bg1 = bg
fg1 = '#166fc9'
bdw = 3
bdc = '#368fe9'
co = 25

# text Colors
bg3 = bg
fg3 = '#3322dd'
textco = 'white'
_w = 20
_w2 = 20

def startup1():
    global _w
    _w += 5
    if _w < 450:
        t.configure(width=_w)
    root.after(5, startup1)

def startup2():
    global _w2
    _w2 += 5
    if _w2 < 450:
        t2.configure(width=_w2)
    root.after(5, startup2)

root = CTk()
root.geometry('1050x800')
root.title('translator v1.0')
root.config(bg=bg)

language_values = list(LANGUAGES.values())


combo1 = CTkComboBox(root,
                     dropdown_hover_color=bg,
                     dropdown_text_color=fg3,
                     border_color=bdc,
                     bg_color=bg,
                     border_width=bdw,
                     fg_color=fg3,
                     text_color=textco,
                     width=120,
                     values=language_values)
combo2 = CTkComboBox(root,
                     dropdown_text_color=fg3,
                     border_color=bdc,
                     bg_color=bg,
                     border_width=bdw,
                     fg_color=fg3,
                     text_color=textco,
                     width=120,
                     values=language_values)

t = CTkTextbox(root,
               corner_radius=co,
               border_width=5,
               bg_color=bg3,
               fg_color=fg3,
               border_color=bdc,
               wrap=WORD,
               font=('', 15, 'bold'),
               text_color=textco,
               width=_w, height=300)
t2 = CTkTextbox(root,
                corner_radius=co,
                border_width=5,
                bg_color=bg3,
                fg_color=fg3,
                border_color=bdc,
                wrap=WORD,
                font=('', 15, 'bold'),
                text_color=textco,
                width=_w2, height=300)

label1 = CTkLabel(root,
                  text=" ",
                  font=("", 20, 'bold'),
                  text_color=textco,
                  fg_color=bg)
label2 = CTkLabel(root,
                  text=" ",
                  font=("", 20, 'bold'),
                  text_color=textco,
                  fg_color=bg)

label12 = CTkLabel(root,text="Translator!",
                   font=('',50,'bold'))
btn = CTkButton(root,text="Translate",
                width=50,height=30)

def label_change():
    global c1,c2
    c1 = combo1.get()
    c2 = combo2.get()
    label1.configure(text=c1)
    label2.configure(text=c2)
    root.after(1,label_change)
# Packs - places
combo1.place(x=300, y=160)
combo2.place(x=860, y=160)
label1.place(x=205, y=160)
label2.place(x=760, y=160)
label12.place(x=100,y=20)
btn.place(x=270,y=540)
t.place(x=15, y=200)
t2.place(x=580, y=200)

# Startup animations
label_change()
startup1()
startup2()
root.mainloop()
