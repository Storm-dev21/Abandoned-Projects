from tkinter import *
from tkinter import messagebox
from customtkinter import *
from PIL import Image
root = CTk()
root.geometry("905x740+500+100"),root.title("UI-designer v1.0"),root.resizable(0,0)
#-Tabs
tabview = CTkTabview(root,bg_color="#ABD6FF",
                     fg_color="#0094FF",
                     segmented_button_fg_color="#0094FF",
                     segmented_button_unselected_color="#0094FF",
                     segmented_button_selected_color="#ABD6FF",
                     text_color="white",
                     segmented_button_selected_hover_color="#8FB5FF",
                     segmented_button_unselected_hover_color="#E3F0FF")
tabview.add("Button Editor")
tabview.add("Frame Editor")
#-images
ButtonEditor = CTkImage(light_image=Image.open("Assets\\texters\\Frames\\MainEditFrame.png"),size=(900,679))
ButtonShow   = CTkImage(light_image=Image.open("Assets\\texters\\Buttons\\Show.png"),size=(79,40))
ButtonCopy   = CTkImage(light_image=Image.open("Assets\\texters\\Buttons\\Copy.png"),size=(136,45))

#-functions

#---ButtonEditor Functions---#
def test(): #تحديد الهيكل الأساسي 
    global type1,type2
    try:
        type1  = chek.get()
        type2  = chek2.get()

        if type1 == True:
            type1 = CTkButton 
            def orgco():
                chek.configure(text_color="#0094FF",text="CTk")
            chek.configure(text_color="lime",text="CTk Selected")
            ButtonEditorbg.after(500,orgco)
        if type2 == True:
            type2 = Button
            def orgco3():
                chek2.configure(text_color="#0094FF",text="Tk")
            chek2.configure(text_color="lime",text="Tk Selected")
            ButtonEditorbg.after(500,orgco3)
    except Exception:
        messagebox.showerror("ERROR!","Please chouse one!")
def show():
    if type1 == True:
        print("its customtkinter")
        try:
        #فلترة المدخلات 
            bg=bgco.get() 
            test =  CTkButton(result,bg_color=bg)
        except Exception:
            def OrgColor():
                bgco.configure(text_color="#0094FF",bg_color="#DFE5FF",border_color="#0094FF",fg_color="#DFE5FF",placeholder_text_color="#0094FF")
                bglab.configure(text_color="#0094FF",text="BackgroundCO",fg_color="#DFE5FF")
            bgco.configure(text_color="red",bg_color="red",border_color="red",fg_color="black",placeholder_text_color="red")
            bglab.configure(text_color="black",text="◖◉ Error ◉◗",fg_color="red")
            ButtonEditorFRAME.after(3000,OrgColor)
        #try:
        #    hightlight=DFCOT.get()
        #    test = Button(result,highlightcolor=hightlight)
        #except Exception:
        #    def OrgColor():
        #        DFCOT.configure(text_color="#0094FF",bg_color="#DFE5FF",border_color="#0094FF",fg_color="#DFE5FF",placeholder_text_color="#0094FF")
        #        DfclabT.configure(text_color="#0094FF",text="HFGC(Tk-only)",fg_color="#DFE5FF")
        #    DFCOT.configure(text_color="red",bg_color="red",border_color="red",fg_color="black",placeholder_text_color="red")
        #    DfclabT.configure(text_color="black",text="◖◉ Error ◉◗",fg_color="red")
        #    ButtonEditorFRAME.after(3000,OrgColor)

        try:
            fg=fgco.get() 
            test =  CTkButton(result,fg_color=fg)
        except Exception:
            def OrgColor():
                fgco.configure(text_color="#0094FF",bg_color="#DFE5FF",border_color="#0094FF",fg_color="#DFE5FF",placeholder_text_color="#0094FF")
                fglab.configure(text_color="#0094FF",text="ForegroundCO",fg_color="#DFE5FF")
            fgco.configure(text_color="red",bg_color="red",border_color="red",fg_color="black",placeholder_text_color="red")
            fglab.configure(text_color="black",text="◖◉ Error ◉◗",fg_color="red")
            ButtonEditorFRAME.after(3000,OrgColor)


        button = CTkButton(result,bg_color=bg,fg_color=fg,width=19,height=10)
        button.place(x=225,y=50)
    if type2 == True:
        print("its tkinter")
def D():
    root.destroy()
    exit()


#----ButtonEditor---#############*
ButtonEditorFRAME = CTkFrame(tabview.tab("Button Editor"))   #mainbody
ButtonEditorbg    = CTkLabel(ButtonEditorFRAME,image=ButtonEditor,text=" ")

show = CTkButton(ButtonEditorFRAME,command=show,hover_color="#DEF0FF",bg_color='white',image=ButtonShow,text="",border_color="#DEF0FF",border_width=0,corner_radius=0,width=79,height=40,fg_color="white")
show.place(x=600,y=337)
copy = CTkButton(ButtonEditorFRAME,hover_color="#DEF0FF",bg_color='white',image=ButtonCopy,text="",border_color="#DEF0FF",border_width=0,corner_radius=0,width=136,height=45,fg_color="white")
copy.place(x=450,y=335)
LABEL = CTkLabel(ButtonEditorbg,text="Button",font=('Calibri',30),text_color="white",bg_color="#66BCFF",width=25,height=35,fg_color="#4194FF",corner_radius=2)
LABEL.place(x=40,y=20)
chek = CTkCheckBox(ButtonEditorbg,command=test,text="CTk",hover_color="#144870",border_color="#0094FF",corner_radius=12,bg_color="#FFFFFF",text_color="#0094FF",fg_color="#80C7FF")
chek.place(x=270,y=272)
chek2 = CTkCheckBox(ButtonEditorbg,command=test,text="Tk",hover_color="#144870",border_color="#0094FF",corner_radius=12,bg_color="#FFFFFF",text_color="#0094FF",fg_color="#80C7FF")
chek2.place(x=270,y=305)
#result-Border
result = CTkFrame(ButtonEditorFRAME,width=520,height=158,fg_color="#C0D1FF",bg_color="#92B4FF",corner_radius=1,border_width=1,border_color="#0094FF")
result.place(x=200,y=440)
#lables (Colors)
bglab = CTkLabel(ButtonEditorbg,text="BackGCO(CTK)",text_color="#0094FF",bg_color="#DFE5FF",width=90,height=10,fg_color="#DFE5FF",corner_radius=2)
fglab = CTkLabel(ButtonEditorbg,text="ForeGCO(CTK)",text_color="#0094FF",bg_color="#DFE5FF",width=90,height=10,fg_color="#DFE5FF",corner_radius=2)
Rellab= CTkLabel(ButtonEditorbg,text="Relif(Tk-only)",text_color="#0094FF",bg_color="#DFE5FF",width=90,height=10,fg_color="#DFE5FF",corner_radius=2)
DfclabT=CTkLabel(ButtonEditorbg,text="HFGC(Tk-only)",text_color="#0094FF",bg_color="#DFE5FF",width=90,height=10,fg_color="#DFE5FF",corner_radius=2)
DbclabT=CTkLabel(ButtonEditorbg,text="HBGC(Tk-only)",text_color="#0094FF",bg_color="#DFE5FF",width=90,height=10,fg_color="#DFE5FF",corner_radius=2)
Afclab= CTkLabel(ButtonEditorbg,text="ActiveF(CTK)",text_color="#0094FF",bg_color="#DFE5FF",width=90,height=10,fg_color="#DFE5FF",corner_radius=2)
ABclab= CTkLabel(ButtonEditorbg,text="ActiveB(CTK)",text_color="#0094FF",bg_color="#DFE5FF",width=90,height=10,fg_color="#DFE5FF",corner_radius=2)
#lables (Body)
wdthlab = CTkLabel(ButtonEditorbg,text="Width",text_color="#0094FF",bg_color="#DFE5FF",width=90,height=10,fg_color="#DFE5FF",corner_radius=2)
highlab = CTkLabel(ButtonEditorbg,text="Hight",text_color="#0094FF",bg_color="#DFE5FF",width=90,height=10,fg_color="#DFE5FF",corner_radius=2)
CornerRl= CTkLabel(ButtonEditorbg,text="CornerR(CTK)",text_color="#0094FF",bg_color="#DFE5FF",width=90,height=10,fg_color="#DFE5FF",corner_radius=2)
borderWL= CTkLabel(ButtonEditorbg,text="Border Width",text_color="#0094FF",bg_color="#DFE5FF",width=90,height=10,fg_color="#DFE5FF",corner_radius=2)
#labels (text)
TextL   = CTkLabel(ButtonEditorbg,text="Text",text_color="#0094FF",bg_color="#DFE5FF",width=90,height=10,fg_color="#DFE5FF",corner_radius=2)
ATextL  = CTkLabel(ButtonEditorbg,text="Active text",text_color="#0094FF",bg_color="#DFE5FF",width=90,height=10,fg_color="#DFE5FF",corner_radius=2)
FontL   = CTkLabel(ButtonEditorbg,text="Font",text_color="#0094FF",bg_color="#DFE5FF",width=90,height=10,fg_color="#DFE5FF",corner_radius=2)

commandL= CTkLabel(ButtonEditorbg,font=('Candara Light',15),text="command",text_color="#0094FF",bg_color="#DFE5FF",width=90,height=10,fg_color="#DFE5FF",corner_radius=2)

#entrys (Colors)
bgco  = CTkEntry(ButtonEditorbg,width=70,height=10,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF",placeholder_text=" . .",placeholder_text_color="#0094FF")  
fgco  = CTkEntry(ButtonEditorbg,width=70,height=10,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF",placeholder_text=" . .",placeholder_text_color="#0094FF") 
Relif = CTkComboBox(ButtonEditorbg,dropdown_text_color="#0094FF",values=[FLAT,RIDGE,GROOVE,SUNKEN,GROOVE],width=70,height=20,fg_color="#DFE5FF",button_color="#DFE5FF",button_hover_color="#144870",dropdown_hover_color="#144870",border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",dropdown_fg_color="#DFE5FF",text_color_disabled="red") 
DFCOT = CTkEntry(ButtonEditorbg,width=70,height=10,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF",placeholder_text=" . .",placeholder_text_color="#0094FF") 
DBGCOT= CTkEntry(ButtonEditorbg,width=70,height=10,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF",placeholder_text=" . .",placeholder_text_color="#0094FF") 
AFCO  = CTkEntry(ButtonEditorbg,width=70,height=10,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF",placeholder_text=" . .",placeholder_text_color="#0094FF") 
ABCO  = CTkEntry(ButtonEditorbg,width=70,height=10,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF",placeholder_text=" . .",placeholder_text_color="#0094FF") 
#Buttons (Colors)
bgB  = CTkButton(ButtonEditorbg,text="info",width=50,height=10,border_width=2,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF")  
fgB  = CTkButton(ButtonEditorbg,text="info",width=50,height=10,border_width=2,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF")  
RFB  = CTkButton(ButtonEditorbg,text="info",width=50,height=10,border_width=2,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF")  
RFB  = CTkButton(ButtonEditorbg,text="info",width=50,height=10,border_width=2,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF")  
DFGB = CTkButton(ButtonEditorbg,text="info",width=50,height=10,border_width=2,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF")  
DBCB = CTkButton(ButtonEditorbg,text="info",width=50,height=10,border_width=2,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF")  
AFCB = CTkButton(ButtonEditorbg,text="info",width=50,height=10,border_width=2,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF")  
ABCB = CTkButton(ButtonEditorbg,text="info",width=50,height=10,border_width=2,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF")  
#Entry (Body)
WDTH   = CTkEntry(ButtonEditorbg,width=70,height=10,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF",placeholder_text=" . .",placeholder_text_color="#0094FF")  
HIGHT  = CTkEntry(ButtonEditorbg,width=70,height=10,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF",placeholder_text=" . .",placeholder_text_color="#0094FF")  
CornerR= CTkEntry(ButtonEditorbg,width=70,height=10,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF",placeholder_text=" . .",placeholder_text_color="#0094FF")  
BorderW= CTkEntry(ButtonEditorbg,width=70,height=10,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF",placeholder_text=" . .",placeholder_text_color="#0094FF")  
#Buttons(Colors)
WDTHB   = CTkButton(ButtonEditorbg,text="info",width=40,height=10,border_width=2,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF")  
HIGHTB  = CTkButton(ButtonEditorbg,text="info",width=40,height=10,border_width=2,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF")  
CORNERB = CTkButton(ButtonEditorbg,text="info",width=40,height=10,border_width=2,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF")  
BorderWB= CTkButton(ButtonEditorbg,text="info",width=40,height=10,border_width=2,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF")  
#Entry (Text)
Text1   = CTkEntry(ButtonEditorbg,width=70,height=10,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF",placeholder_text=" . .",placeholder_text_color="#0094FF")  
TextA   = CTkEntry(ButtonEditorbg,width=70,height=10,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF",placeholder_text=" . .",placeholder_text_color="#0094FF")  
Font    = CTkEntry(ButtonEditorbg,width=70,height=10,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF",placeholder_text=" . .",placeholder_text_color="#0094FF")  
#Button (text)
textB    = CTkButton(ButtonEditorbg,text="info",width=40,height=10,border_width=2,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF")  
textAB   = CTkButton(ButtonEditorbg,text="info",width=40,height=10,border_width=2,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF")  
FontB    = CTkButton(ButtonEditorbg,text="info",width=40,height=10,border_width=2,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF")  
command  = CTkEntry(ButtonEditorbg,width=100,height=10,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF",placeholder_text=" . . .",placeholder_text_color="#0094FF")  

bgcoT  = CTkEntry(ButtonEditorbg,width=80,height=10,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF",placeholder_text="BG(Tk-Only)",placeholder_text_color="#0094FF")  
fgcoT  = CTkEntry(ButtonEditorbg,width=80,height=10,border_color="#0094FF",bg_color="#DFE5FF",text_color="#0094FF",fg_color="#DFE5FF",placeholder_text="FG(Tk-Only)",placeholder_text_color="#0094FF") 
bgfgT  = CTkLabel(ButtonEditorbg,text="BG-FG(Tk)",text_color="#0094FF",bg_color="#DFE5FF",width=90,height=10,fg_color="#DFE5FF",corner_radius=2)

#-packs-#(button_editor)#########
ButtonEditorbg.pack() 
 
bglab.place (x=45 ,y=131) #labels (Colors)
bgfgT.place(x=270,y=335)
fglab.place (x=45,y=167)
Rellab.place(x=45,y=203)
DfclabT.place(x=45,y=238)
DbclabT.place(x=45,y=276)
Afclab.place(x=45,y=313)
ABclab.place(x=45,y=348)
wdthlab.place (x=270,y=131) #labels (body)
highlab.place (x=270,y=164)
CornerRl.place(x=270,y=203)
borderWL.place(x=270,y=238)
TextL.place (x=470,y=132) #labels (text)
ATextL.place(x=470,y=168)
FontL.place (x=470,y=204)


commandL.place(x=725,y=132)
bgco.place   (x=135,y=129) #Entrys (Colors)
bgcoT.place  (x=360,y=355)
fgcoT.place  (x=270,y=355)
fgco.place   (x=135,y=165)
Relif.place  (x=135,y=200)
DFCOT.place  (x=135,y=235)
DBGCOT.place (x=135,y=273)
AFCO.place  (x=135,y=310)
ABCO.place  (x=135,y=345)
bgB.place   (x=210,y=129) #Buttons(Colors)
fgB.place   (x=210,y=165)
RFB.place   (x=210,y=200)
DFGB.place  (x=210,y=235)
DBCB.place  (x=210,y=273)
AFCB.place  (x=210,y=310)
ABCB.place  (x=210,y=345)
WDTH.place   (x=360,y=129) #Entrys(Body)
HIGHT.place  (x=360,y=161)
CornerR.place(x=360,y=200)
BorderW.place(x=360,y=235)
WDTHB.place   (x=435,y=129) #Buttons(Body)
HIGHTB.place  (x=435,y=161)
CORNERB.place (x=435,y=200)
BorderWB.place(x=435,y=235)
Text1.place(x=550,y=129) #Entrys(text)
TextA.place(x=550,y=165)
Font.place (x=550,y=200)
textB.place (x=630,y=129) #Button ()
textAB.place(x=630,y=165)
FontB.place (x=630,y=200)
command.place(x=720,y=165)
#-------------------#############*

#packs-places(mains)
tabview.pack(expand=TRUE,fill=BOTH)
ButtonEditorFRAME.pack()

root.mainloop()