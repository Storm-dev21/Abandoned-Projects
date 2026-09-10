import parso
from customtkinter import *
from tkinter import Button , Frame , messagebox , PhotoImage
global LANG
# == themes == #
global ButtonColor , Tcolor , TLabelCo , Font , CO , Tlabel , ATbuttons , TbuttonsCO , BG , sT , TlangBtn , TlabelLANG , LANG_frame , FrameCO , Bd_Co , TXco , Tfont , ENFont
# == lang == #
global settingsBtn , exitButton
#change the langs

class Languages:
    def __init__(self):
        pass
    def arbic(self):
        global settingsBtn , exitButton , title , TlangBtn , TlabelLANG , ENlabel 
        #buttons
        
        #Tops
        settingsBtn = 'الاعدادات'
        exitButton  = 'خروج'
        #settings
        title       = 'الاعدادات'
        TlangBtn    = '          اللغة' 
        TlabelLANG  = '                                                                        اللغة اختر'
        ENlabel     = 'التشفير'
    def english(self):
        global settingsBtn , exitButton , title , TlangBtn , TlabelLANG , ENlabel 
        #buttons
        
        #Tops
        settingsBtn = 'settings'    
        exitButton  = 'exit'
        #settings
        title       = 'settings'
        TlangBtn    = 'Language       ' 
        TlabelLANG  = 'pick a Language'
        #Down stuff 
        ENlabel     = 'Encryption'
    def __init__(self):
        pass
class Themes:
    def __init__(self):
        pass
    def rick_theme(self):
        global ButtonColor , Tcolor , TLabelCo , Font , CO , Tlabel , ATbuttons , TbuttonsCO , BG , sT , LANG_frame , FrameCO , Bd_Co , TXco , Tfont , ENFont
        #TOP colors#  -color-          -where-
        ATbuttons   = "green"           #avtive Top Buttons color 
        TbuttonsCO  = '#B4E4FD'         #Top Buttons Colors
        Tlabel      = 'rick Theme'      #top
        TLabelCo    = '#B4E4FD'         #Top
        Tcolor      = "white"           #text color
        Font        = ('Cascadia Mono',25,'bold')
        sT          = '#B4E4FD'         #settings text title color
        CO          = 10                #cornerRidus
        BG          = 'white'         
        LANG_frame   = 'black'           #flag frame
        #Down Colors
        ButtonColor = 'green'            #Button color
        FrameCO     = '#252525'          #frame color
        Bd_Co       = '#4CFF00'          #BorderCo(Frame)
        TXco        = '#4CFF00'          #DownLabels 
        Tfont       = ('Cascadia Code',26,'bold')
        ENFont      = ('Cascadia Code',20,)
    def morty_theme(self):
        pass
#imports -  type 
    
themes    =  Themes()      #import themes
themes    .  rick_theme()  # the theme
Language  =  Languages()   #import lang      
LANG      = Language




LANG.english()
# === defines ===  # 
def exit():               # - save before exit? - #
    x = messagebox.askyesno("schwify cipher v1.0",'are you sure u wanna Exit?')
    if   x == True:
        window.destroy()
        quit()
    elif x == False:
        pass
    else:
        pass
def settings():           # - main settings     - #
    settings   = CTk ()
    settings.geometry('1280x720+1+10')
    settings.config  (bg=BG)
    settings.title   ('schwify cipher-settings')
    titleLabel = CTkLabel(settings,bg_color=BG,text=title,text_color=sT,font=Font).place(x=50,y=50)
    # == define == #
    def langS():   #choose lang
        for child in settings.winfo_children(): 
            child.destroy() 
        labelLANG = CTkLabel (settings,bg_color=BG,text=TlabelLANG,text_color=sT,font=Font).place(x=50,y=50) #main label
        def arbic():
            messagebox.showinfo('!warn','lang will be set to arbic\nporogram will shutdown')
            with open("main.py", 'r') as file:
                file_content = file.read()
            lines = file_content.split('\n')  #68   75
            lines[75] = lines[75].replace('LANG.english()', 'LANG.arbic()')
            modified_content = '\n'.join(lines)
            with open('main.py', 'w') as file:
                file.write(modified_content)
            exit()

        def english():
            messagebox.showinfo('!warn','lang will be set to english\nporogram will shutdown')
            with open("main.py", 'r') as file:
                file_content = file.read()
            lines = file_content.split('\n')
            lines[75] = lines[75].replace('LANG.arbic()', 'LANG.english()')
            modified_content = '\n'.join(lines)
            with open('main.py', 'w') as file:
                file.write(modified_content)
            exit()

        AR        = CTkButton(settings,text="Arbic",  corner_radius=CO,bg_color=BG,text_color=Tcolor,fg_color=TbuttonsCO,hover_color=ATbuttons,font=Font,width=245,height=40,command=arbic).place(x=100,y=100) #arbic btn
        EN        = CTkButton(settings,text="English",corner_radius=CO,bg_color=BG,text_color=Tcolor,fg_color=TbuttonsCO,hover_color=ATbuttons,font=Font,width=245,height=40,command=english).place(x=400,y=100) #english btn
    #Var         -Type-   -master- -cornertRadius-   -bg color-  -text color-     -fg color-          -ActiveColor-          -text-         -font-     -width x hight-    -command-     -place- 
    langBtn    = CTkButton(settings,corner_radius=CO,bg_color=BG,text_color=Tcolor,fg_color=TbuttonsCO,hover_color=ATbuttons,text=TlangBtn, font=Font,width=245,height=40,command=langS).place(x=50,y=100)
    settings.mainloop()
def wait():               # - wait    
    
    x = messagebox.askyesno("Wait",'are u sure u wanna exit?')
    if   x == True:
        window.destroy()
        quit()
    elif x == False:
        pass
    else:
        pass
# ==== Window ==== # 
window = CTk() 
window.geometry  ('1920x1080+1+1'          )
window.attributes("-fullscreen",False      )
window.title     ('schwify cipher v1.0'    )
window.config    (background=BG            )
window.protocol  ("WM_DELETE_WINDOW", wait )
##window.iconbitmap('')
# == wigets == #   Top (32-38) 
logo     = PhotoImage(file =r'Images\\logoImage.png').subsample    (x=1,y=1)
labelogo = CTkLabel  (window,text=" ",image=logo,bg_color=BG).place(x=5,y=30)
label = CTkLabel (window,text_color=Tcolor,font=('Cascadia Mono',11,'bold'),text=Tlabel,bg_color=TLabelCo).pack(fill=BOTH,side=TOP) #Main Label
#VarTOP -Type-    -master- -cornertRadius- -bg color-  -text color-     -fg color-          -ActiveColor-        -text-           -font-     -width x hight-    -command-   -place- 
EXb   = CTkButton(window,corner_radius=CO,bg_color=BG,text_color=Tcolor,fg_color=TbuttonsCO,hover_color=ATbuttons,text=exitButton,    font=Font,width=235,height=60,command=exit).place(x=1400,y=40)    #exit 
STb   = CTkButton(window,corner_radius=CO,bg_color=BG,text_color=Tcolor,fg_color=TbuttonsCO,hover_color=ATbuttons,text=settingsBtn,font=Font,width=235,height=60,command=settings).place(x=1650,y=40)   #settings 

#-DOWN_wegits - Main stuff ( as labels and frame )
Dframe= CTkFrame(window,width=1879,height=790,fg_color=FrameCO,bg_color=BG,border_color=Bd_Co,border_width=6,corner_radius=CO).place(x=20,y=220)
DLABEL= CTkLabel(Dframe,text=ENlabel,text_color=TXco,font=Tfont).place(x=50,y=250)
#var    -Type-     -master-   -text-     -width x hight-  -place-
EN_enter = CTkEntry(Dframe,placeholder_text="text ..",font=ENFont).place(x=50,y=300)




window.mainloop()
