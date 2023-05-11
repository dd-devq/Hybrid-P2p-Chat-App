# SIMPLE P2P CHAT - LOGIN PAGE
import tkinter
from tkinter import *
from theme import *

class login_window:
    def __init__(self):
        #define Login window
        self.login_page = tkinter.Tk()
        self.login_page.title("Simple P2P Chat application - Login")
        self.login_page.geometry("600x300")
        self.login_page.resizable(0,0)

        #set windows colors
        self.login_page.config(bg=darkgreen)

        #Define GUI Layout
        #Create Frames
        self.login_frame = tkinter.Frame(self.login_page, bg=darkgreen)

        self.login_frame.pack(pady= 30)

        #Frame Layout
        self.login_label = tkinter.Label(self.login_frame, text="Login", font=("haveltica", 18), fg=yellow, bg=darkgreen)
        self.uid_label = tkinter.Label(self.login_frame, text="User ID:", font=my_font, fg=yellow, bg=darkgreen)
        self.uid_entry = tkinter.Entry(self.login_frame, borderwidth=0, font=my_font)
        self.pw_label = tkinter.Label(self.login_frame, text="Password:", font=my_font, fg=yellow, bg=darkgreen)
        self.pw_entry = tkinter.Entry(self.login_frame, borderwidth=0, font=my_font, show = '*')
        self.signin_button = tkinter.Button(self.login_frame, text="Sign in", font=my_font, fg = black, bg=yellow, borderwidth=0, width=10, height=3, command=lambda: self.test_multi_win())
        self.register_button = tkinter.Button(self.login_frame, text="Register", font=my_font_small, fg = white, bg=lightgreen, borderwidth=0, width=8)
        self.forgotpw_button = tkinter.Button(self.login_frame, text="Forgot password", font=my_font_small, fg = white, bg=lightgreen, borderwidth=0, width= 16)
        self.showpasswd_button = tkinter.Checkbutton(self.login_frame, text="Show password", font=my_font_small, fg="orange", bg = darkgreen, activebackground=darkgreen, command = lambda: self.show_passwd(self.pw_entry), anchor = 'w')

        self.login_label.grid(row = 0, column = 0, columnspan = 4, padx = 2, pady = 10)
        self.uid_label.grid(row=1, column=0, padx=2, pady=5)
        self.uid_entry.grid(row=1, column=1, columnspan= 2, padx=2, pady=5)
        self.pw_label.grid(row=2, column=0, padx=2, pady=5)
        self.pw_entry.grid(row=2, column=1, columnspan= 2, padx=2, pady=5)
        self.signin_button.grid(row=1, column=3, rowspan = 2, padx=10, pady=5)
        self.showpasswd_button.grid(row = 3, column=1, columnspan = 2, padx = 10, pady = 5)
        self.register_button.grid(row=4, column=1, padx=10, pady=5)
        self.forgotpw_button.grid(row=4, column=2, padx=10, pady=5)

    def show_passwd(self, entry_field):
        if entry_field.cget('show') == '*':
            entry_field.config(show='')
        else:
            entry_field.config(show='*')

    def test_multi_win(self):
        frlist_window(['huy', 'hoang'], ['loc', 'khanh', 'bao'])
        self.login_page.destroy()


    def render(self):
        self.login_page.mainloop()

class frlist_window:
    def __init__(self, onlinelist, offlinelist):
        self.updatelist(onlinelist, offlinelist)

        #define FRIEND LIST window
        self.flist_page = tkinter.Tk()
        self.flist_page.title("Simple P2P Chat application - Friends List")
        self.flist_page.geometry("700x800")
        self.flist_page.resizable(0,0)

        #set window colors
        self.flist_page.config(bg=darkgreen)

        #Define GUI Layout
        #Create Frames
        self.info_frame = tkinter.Frame(self.flist_page, bg=yellow)
        self.label_frame = tkinter.Frame(self.flist_page, bg = darkgreen)
        self.search_frame = tkinter.Frame(self.flist_page, bg=white)
        self.list_frame = tkinter.Frame(self.flist_page, bg=white)
        self.button_frame = tkinter.Frame(self.flist_page, bg = white)
        

        self.info_frame.pack(pady = 15)
        self.label_frame.pack(pady = 0)
        self.search_frame.pack(pady = 10)
        self.list_frame.pack()
        self.button_frame.pack(pady = 5)

        # Info Frame Layout
        self.name_label = tkinter.Label(self.info_frame, text = "User ID:", font=my_font, fg=darkgreen, bg=yellow, width= 10, anchor = "nw")
        self.name = tkinter.Label(self.info_frame, text = "hoangtran12902", font=my_font, fg=darkgreen, bg=yellow, width=44, anchor = "nw")
        self.mail_label = tkinter.Label(self.info_frame, text = "User Email:", font=my_font, fg=darkgreen, bg=yellow, width= 10, anchor = "nw")
        self.mail = tkinter.Label(self.info_frame, text = "hoang.tran12902@gmail.com", font=my_font, fg=darkgreen, bg=yellow, width=44, anchor = "nw")

        self.name_label.grid(row = 0 , column=0, padx = 5, pady = 5)
        self.name.grid(row = 0 , column=1, columnspan= 2, padx = 5, pady = 5)
        self.mail_label.grid(row = 1 , column=0, padx = 5, pady = 5)
        self.mail.grid(row = 1 , column=1, columnspan= 2, padx = 5, pady = 5)

        #Label Frame Layout
        self.friend_list_label = tkinter.Label(self.label_frame, text = "Friend List", font=('haveltica', 18), fg=white, bg=darkgreen, width= 30, anchor = "nw")
        self.frrequest_button = tkinter.Button(self.label_frame, text = "Friend request", borderwidth = 0, width = 10, font = my_font_small, bg = yellow, fg = black)
        self.addfr_button = tkinter.Button(self.label_frame, text = "Add friend", borderwidth = 0, width = 10, font = my_font_small, bg = yellow, fg = black)
        self.friend_list_label.grid(row = 0 , column=0, padx = 5, pady = 5)
        self.frrequest_button.grid(row = 0 , column=1, padx = 5, pady = 5)
        self.addfr_button.grid(row = 0 , column=2, padx = 5, pady = 5)

        #List Frame Layout
        self.my_scrollbar = tkinter.Scrollbar(self.list_frame, orient=VERTICAL)
        self.my_listbox = tkinter.Listbox(self.list_frame, height=20, width=55, borderwidth=0, bg=white, fg=darkgreen, font=my_font, yscrollcommand=self.my_scrollbar.set)
        self.my_scrollbar.config(command=self.my_listbox.yview)
        self.my_listbox.grid(row=0, column=0)
        self.my_scrollbar.grid(row=0, column=1, sticky="NS")

        #Search Frame Layout
        self.input_entry = tkinter.Entry(self.search_frame, width=44, borderwidth=0, font=my_font)
        self.search_button = tkinter.Button(self.search_frame, text="Search", borderwidth=0, width=10, font=my_font, bg=yellow, fg = black)
        self.input_entry.grid(row=0, column=0, padx=5, pady=5)
        self.search_button.grid(row=0, column=1, padx=5, pady=5)
        self.input_entry.bind("<KeyRelease>", self.search_check)
        self.search_button.bind("<Button-1>", self.search_check)

        #Button Frame Layout
        self.unfriend_button = tkinter.Button(self.button_frame, text = "Unfriend", width=27, borderwidth = 0, font = my_font, bg = yellow, fg = black)
        self.chat_button = tkinter.Button(self.button_frame, text = "Start chatting", width = 27, borderwidth = 0, font = my_font, bg = yellow, fg = black)
        self.unfriend_button.grid(row=0, column=0,padx=5, pady=5)
        self.chat_button.grid(row=0, column=1, padx=5, pady=5)
        self.update_displaylist(self.onlinelist, self.offlinelist)

    def updatelist(self, onlinelist, offlinelist):
        self.onlinelist = onlinelist
        self.offlinelist = offlinelist

    def search_check(self, event):
        typed = self.input_entry.get()
        if type == '':
            self.update_displaylist(self.onlinelist, self.offlinelist)
        else:
            online_tmplist = []
            offline_tmplist = []
            for user in self.onlinelist:
                if typed.lower() in user.lower():
                    online_tmplist.append(user)
            for user in self.offlinelist:
                if typed.lower() in user.lower():
                    offline_tmplist.append(user)
            self.update_displaylist(online_tmplist, offline_tmplist)

    def update_displaylist(self, onlinelist, offlinelist):
        self.my_listbox.delete(0, END)
        for user in onlinelist:
            self.my_listbox.insert(0, user)
            self.my_listbox.itemconfig(0,{'fg':'green2'})
        for user in offlinelist:
            self.my_listbox.insert(END, user)
            self.my_listbox.itemconfig(END,{'fg':'gray63'})

    def render(self):
        #Run the self.flist_page window's mainloop()
        self.flist_page.mainloop()

#friendlist_window = frlist_window(onlinelist, offlinelist)
#friendlist_window.render()

login_page = login_window()
login_page.render()



