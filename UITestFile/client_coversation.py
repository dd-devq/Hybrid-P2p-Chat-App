# SIMPLE P2P CHAT - CONVERSATION
import tkinter, socket, threading
from tkinter import DISABLED, VERTICAL, END, NORMAL
from theme import *
from tkinter.messagebox import askyesno, showerror
from tkinter import filedialog

class conversation_window:
    def __init__(self):
        #define CONVERSATION window
        self.conver_page = tkinter.Tk()
        self.conver_page.title("Simple P2P Chat application - Conversation")
        self.conver_page.geometry("700x700")
        self.conver_page.resizable(0,0)

        #set window colors
        self.conver_page.config(bg=darkgreen)

        #Define GUI Layout
        #Create Frames
        self.info_frame = tkinter.Frame(self.conver_page, bg=yellow)
        self.label_frame = tkinter.Frame(self.conver_page, bg = darkgreen)
        self.input_frame = tkinter.Frame(self.conver_page, bg=white)
        self.output_frame = tkinter.Frame(self.conver_page, bg=white)

        self.info_frame.pack(pady = 10)
        self.label_frame .pack(pady = 10)
        self.output_frame.pack(pady = 10)
        self.input_frame.pack()

        # Info Frame Layout
        self.name_label = tkinter.Label(self.info_frame, text = "User ID:", font=my_font, fg=darkgreen, bg=yellow, width= 10, anchor = "nw")
        self.name = tkinter.Label(self.info_frame, text = "hoangtran12902", font=my_font, fg=darkgreen, bg=yellow, width=44, anchor = "nw")
        self.mail_label = tkinter.Label(self.info_frame, text = "User Email:", font=my_font, fg=darkgreen, bg=yellow, width= 10, anchor = "nw")
        self.mail = tkinter.Label(self.info_frame, text = "hoang.tran12902@gmail.com", font=my_font, fg=darkgreen, bg=yellow, width=44, anchor = "nw")

        self.name_label.grid(row = 0 , column=0, padx = 5, pady = 5)
        self.name.grid(row = 0 , column=1, columnspan= 2, padx = 5, pady = 5)
        self.mail_label.grid(row = 1 , column=0, padx = 5, pady = 5)
        self.mail.grid(row = 1 , column=1, columnspan= 2, padx = 5, pady = 5)

        self.friend_list_label = tkinter.Label(self.label_frame , text = "Chatting with huyhoang0512", font=('haveltica', 18), fg=white, bg=darkgreen, width=44, anchor = "nw")
        self.friend_list_label.grid(row = 0 , column=0, padx = 5, pady = 5)

        #Output Frame Layout
        self.my_scrollbar = tkinter.Scrollbar(self.output_frame, orient=VERTICAL)
        self.my_listbox = tkinter.Listbox(self.output_frame, height=20, width=55, borderwidth=0, bg=white, fg=darkgreen, font=my_font, yscrollcommand=self.my_scrollbar.set)
        self.my_scrollbar.config(command=self.my_listbox.yview)
        self.my_listbox.grid(row=0, column=0)
        self.my_scrollbar.grid(row=0, column=1, sticky="NS")

        #Input Frame Layout
        self.input_entry = tkinter.Entry(self.input_frame, width=39, borderwidth=0, font=my_font)
        self.file_button = tkinter.Button(self.input_frame, text="File", borderwidth=0, width=7, font=my_font, bg=yellow, fg = black, command=lambda: self.get_file())
        self.send_button = tkinter.Button(self.input_frame, text="Send", borderwidth=0, width=7, font=my_font, bg=yellow, fg = black)
        self.input_entry.grid(row=0, column=0, padx=5, pady=5)
        self.file_button.grid(row=0, column=1, padx=5, pady=5)
        self.send_button.grid(row=0, column=2, padx=5, pady=5)

        #Pop up confirm message when quit
        self.conver_page.protocol("WM_DELETE_WINDOW", self.close_confirm)

    def close_confirm(self):
        confirm_reply = askyesno(title="Leave conversation?", message="You will disconnect with this user and the conversation will be deleted when you close this window!\nDo you want to close?")
        #confirm_reply = showerror(title="Message syntax error!", message="Please do not start a message with 'FILE: '!")
        if confirm_reply:
            self.conver_page.destroy()

    def get_file(self):
        self.filename = filedialog.askopenfilename(title='Select a file')
        #tkinter.Label(tkinter.Toplevel(), text = self.filename).pack()

    def render(self):
        #Run the self.conver_page window's mainloop()
        self.conver_page.mainloop()

test = conversation_window()
test.render()