from customtkinter import *
from tkinter import *
from tkinter import messagebox, filedialog
import os
import requests

class DiscordSpammer:
    def __init__(self, root):
        self.root = root
        self.root.title('Discord-Spammer 0.1')
        self.root.geometry('1920x1080+-2+1')
        self.root.maxsize(1920, 1080)
        self.root.config(bg="black")
        self.root.protocol("WM_DELETE_WINDOW", self.wait)
        
        self.channel_id_list = []
        self.tokens = []
        self.spam_times = 1
        
        self.setup_ui()
    
    def wait(self):
        quest = messagebox.askyesno('Wait!', 'Are you sure you want to exit?')
        if quest:
            self.root.destroy()
            exit()
    
    def token(self):
        token = self.TokenEntry.get().strip()
        if token:
            with open('tokens.txt', 'a') as e:
                e.write(token + '\n')
            self.TokenEntry.delete(0, END)
        else:
            messagebox.showwarning("Input Error", "Token entry is empty. Please provide a token.")
    
    def sp0am(self):
        content = self.message.get("1.0", END).strip()
        try:
            times = self.spam_times
        except ValueError:
            self.TimesEntry.configure(placeholder_text="int only!", fg_color='red')
            return

        if not self.tokens:
            messagebox.showwarning("No Tokens", "No tokens have been provided. Please add tokens before proceeding.")
            return

        if not self.channel_id_list:
            messagebox.showwarning("No Channels", "No channel IDs have been provided. Please add channel IDs before proceeding.")
            return

        for i in range(times):
            for token in self.tokens:
                for channel_id in self.channel_id_list:
                    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
                    headers = {'Authorization': f'Bot {token}'}  # Adjust this if using user tokens
                    payload = {'content': content}
                    response = requests.post(url, json=payload, headers=headers)
                    if response.status_code == 200:
                        print('sent')
                    else:
                        print('failed', response.status_code, response.text)
    
    def search(self):
        token_list = filedialog.askdirectory(title='Select Directory')
        if token_list:
            self.TokenEntryList.insert(0, token_list)
            name = 'tokens.txt'
            file_path = self.find(name, token_list)
            if file_path:
                self.tokens = self.read_tokens(file_path)
                with open('tokens.txt', 'w') as r:
                    r.write('\n'.join(self.tokens))
    
    def read_tokens(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return f.read().strip().split('\n')
        except FileNotFoundError:
            messagebox.showerror('Error', f'The file {file_path} was not found.')
            return []
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {e}')
            return []

    def addlist(self):
        token_list = self.TokenEntryList.get().strip()
        if token_list:
            name = 'tokens.txt'
            file_path = self.find(name, token_list)
            if file_path:
                self.tokens = self.read_tokens(file_path)
                with open('tokens.txt', 'w') as r:
                    r.write('\n'.join(self.tokens))
        else:
            messagebox.showwarning("Input Error", "Path entry is empty. Please provide a path to the tokens file.")

    def add_channel_id(self):
        channel_id = self.ChannelIDEntry.get().strip()
        if channel_id:
            self.channel_id_list.append(channel_id)
            self.ChannelIDEntry.delete(0, END)
        else:
            messagebox.showwarning("Input Error", "Channel ID entry is empty. Please provide a channel ID.")

    def find(self, name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)
        self.TokenEntryList.delete(0, END)
        self.tokenLabList.configure(text="Error, file not found! (make sure it's tokens.txt)", text_color='red', font=('Cascadia Code', 20))
        self.TokenEntryList.configure(fg_color='darkred', border_color='black')
        self.TokenEntryList.after(2000, lambda: self.reset_token_entry_list())
        return None

    def reset_token_entry_list(self):
        self.TokenEntryList.configure(fg_color='black', border_color='lime')
        self.tokenLabList.configure(text="Import list of tokens", text_color="lime", font=('Cascadia Code', 30))

    def times(self):
        try:
            self.spam_times = int(self.TimesEntry.get().strip())
            self.TimesEntry.configure(placeholder_text="int only!", fg_color='green')  # Indicate success
        except ValueError:
            self.TimesEntry.configure(placeholder_text="int only!", fg_color='red')

    def setup_ui(self):
        # logo
        try:
            self.Logo = PhotoImage(file=r'LOGO.png')
            self.l = self.Logo.subsample(x=1, y=1)
        except Exception as e:
            print(f"Error loading image: {e}")
            self.l = None

        # Frames
        LogoFrame = Frame(self.root, height=300, width=923, bg='black')
        MainFrame = CTkFrame(self.root, height=650, width=1910, bg_color='black', fg_color='black', border_color='lime', border_width=2, corner_radius=50)
        DownFrame = CTkFrame(self.root, height=20, width=1910, bg_color='lime', fg_color='lime', border_color='lime', border_width=10, corner_radius=12)
        TokenFrame = CTkFrame(MainFrame, height=550, width=750, bg_color='black', fg_color='black', border_color='lime', border_width=2, corner_radius=50)
        ChannelIDFrame = CTkFrame(MainFrame, height=200, width=660, bg_color='black', fg_color='black', border_color='lime', border_width=2, corner_radius=50)

        # Labels
        if self.l:
            self.LogoLable = Label(LogoFrame, image=self.l, bg='black')
        else:
            self.LogoLable = Label(LogoFrame, text="Logo not found", bg='black', fg='red')
        tokenLab = CTkLabel(TokenFrame, text="Tokens", text_color="lime", font=('Cascadia Code', 30))
        self.tokenLabList = CTkLabel(TokenFrame, text="Import list of tokens", text_color="lime", font=('Cascadia Code', 30))
        channelIDlab = CTkLabel(ChannelIDFrame, text="Channel IDs", text_color="lime", font=('Cascadia Code', 20))
        zpam = CTkLabel(MainFrame, text="Spam content", text_color="lime", font=('Cascadia Code', 20))
        TimesLab = CTkLabel(MainFrame, text="Times", text_color="lime", font=('Cascadia Code', 20))

        # Entries
        self.TokenEntry = CTkEntry(TokenFrame, placeholder_text='Paste Token here..', text_color='Lime', font=('Cascadia Code', 20), placeholder_text_color='#73A848', width=530, height=75, bg_color="black",
                              fg_color="black", corner_radius=12, border_color='lime', border_width=4)
        self.TokenEntryList = CTkEntry(TokenFrame, placeholder_text='Path..', text_color='Lime', font=('Cascadia Code', 20), placeholder_text_color='#73A848', width=530, height=75, bg_color="black",
                                  fg_color="black", corner_radius=12, border_color='lime', border_width=4)
        self.ChannelIDEntry = CTkEntry(ChannelIDFrame, placeholder_text='ChannelIDs', text_color='Lime', font=('Cascadia Code', 20), placeholder_text_color='#73A848', width=550, height=60, bg_color="black",
                                  fg_color="black", corner_radius=12, border_color='lime', border_width=4)
        self.TimesEntry = CTkEntry(MainFrame, placeholder_text='int..', text_color='Lime', font=('Cascadia Code', 20), placeholder_text_color='#73A848', width=200, height=40, bg_color="black",
                              fg_color="black", corner_radius=12, border_color='lime', border_width=2)

        # Buttons
        TokenButton = CTkButton(TokenFrame, command=self.token, text='Add', font=('Cascadia Code', 15, 'bold'), width=70, height=75, bg_color='black', fg_color='black', border_color='lime',
                                border_width=4, corner_radius=10, hover_color='#ADFE6B', text_color_disabled='lime', text_color='lime')
        TokenButtonList = CTkButton(TokenFrame, command=self.search, text='Search', font=('Cascadia Code', 15, 'bold'), width=70, height=75, bg_color='black', fg_color='black', border_color='lime',
                                    border_width=4, corner_radius=10, hover_color='#ADFE6B', text_color_disabled='lime', text_color='lime')
        TokenButtonListadd = CTkButton(TokenFrame, command=self.addlist, text='Set', font=('Cascadia Code', 15, 'bold'), width=30, height=75, bg_color='black', fg_color='black', border_color='lime',
                                       border_width=4, corner_radius=10, hover_color='#ADFE6B', text_color_disabled='lime', text_color='lime')
        channelButton = CTkButton(ChannelIDFrame, command=self.add_channel_id, text='Add', font=('Cascadia Code', 15, 'bold'), width=70, height=60, bg_color='black', fg_color='black', border_color='lime',
                                  border_width=4, corner_radius=10, hover_color='#ADFE6B', text_color_disabled='lime', text_color='lime')
        send_button = CTkButton(MainFrame, command=self.sp0am, text='Start', font=('Cascadia Code', 20, 'bold'), width=130, height=80, bg_color='black', fg_color='black', border_color='lime',
                                border_width=4, corner_radius=10, hover_color='#ADFE6B', text_color_disabled='lime', text_color='lime')
        set_button = CTkButton(MainFrame, command=self.times, text='Set', font=('Cascadia Code', 15), width=50, height=30, bg_color='black', fg_color='black', border_color='lime',
                               border_width=2, corner_radius=10, hover_color='#ADFE6B', text_color_disabled='lime', text_color='lime')
        exit_button = CTkButton(self.root, command=self.wait, text='Exit', font=('Cascadia Code', 20, 'bold'), width=200, height=90, bg_color='black', fg_color='black', border_color='lime',
                                border_width=4, corner_radius=10, hover_color='darkgreen', text_color_disabled='lime', text_color='lime')

        # Textbox
        self.message = CTkTextbox(MainFrame, width=620, height=200, font=('Cascadia Code', 15, 'bold'), bg_color='black', fg_color='black', corner_radius=12,
                             border_width=4, border_color='lime', text_color='lime', scrollbar_button_color='#73A848', scrollbar_button_hover_color='lime')

        # Packs-place
        LogoFrame.pack(side=TOP)
        self.LogoLable.pack(side=LEFT, padx=10, pady=10)
        MainFrame.pack(anchor=N)
        DownFrame.pack(side=BOTTOM)
        TokenFrame.place(x=100, y=50)
        tokenLab.place(x=60, y=100)
        self.TokenEntry.place(x=60, y=150)
        TokenButton.place(x=600, y=150)
        self.tokenLabList.place(x=60, y=300)
        self.TokenEntryList.place(x=60, y=350)
        TokenButtonListadd.place(x=680, y=350)
        TokenButtonList.place(x=600, y=350)
        ChannelIDFrame.place(x=1020, y=50)
        channelIDlab.place(x=40, y=40)
        self.ChannelIDEntry.place(x=20, y=80)
        channelButton.place(x=580, y=80)
        zpam.place(x=1040, y=270)
        self.message.place(x=1040, y=300)
        send_button.place(x=1550, y=510)
        self.TimesEntry.place(x=1120, y=530)
        TimesLab.place(x=1050, y=535)
        set_button.place(x=1260, y=535)
        exit_button.place(x=1700, y=20)

if __name__ == "__main__":
    root = CTk()
    app = DiscordSpammer(root)
    root.mainloop()
