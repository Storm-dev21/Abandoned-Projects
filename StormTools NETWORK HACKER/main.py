from customtkinter import *
from PIL import Image


def start_():

    root = CTk()
    root.title("StormTools Network Hacker 1.0")
    root.geometry("1240x773+340+154")
    #root.iconbitmap("")
    root.configure(fg_color="black")

	#images
    Logo=CTkImage(dark_image=Image.open("icons//Logo.png"),size=(412, 100))



    Logo_holder=CTkLabel(master=root,image=Logo,text=" ")
    Logo_holder.pack(anchor="sw")

	

    Main_Frame=CTkFrame(master=root,fg_color="#1E1E1E",width=412, height=900)
    Main_Frame.pack(side="left")
	

    network_Pentester=CTkButton(master=Main_Frame,fg_color="#101010",hover_color="gray",width=400,text_color="white",height=100,text="Network Pentester",font=("Corbel Light",25,"bold"))
    network_Pentester.place(x=5,y=50)


    WIFI_GRABBER=CTkButton(master=Main_Frame,fg_color="#101010",hover_color="gray",width=400,text_color="white",height=100,text="Wifi grabber (malware)",font=("Corbel Light",25,"bold"))
    WIFI_GRABBER.place(x=5,y=170)


    network_Pentester=CTkButton(master=Main_Frame,fg_color="#101010",hover_color="gray",width=400,text_color="white",height=100,text="Network Mapper",font=("Corbel Light",25,"bold"))
    network_Pentester.place(x=5,y=290)


    root.mainloop()



if __name__=="__main__":
    start_()
