# SIMPLE P2P CHAT - CONVERSATION
import tkinter, socket, threading
from tkinter import DISABLED, VERTICAL, END, NORMAL
from theme import *
from tkinter.messagebox import askyesno, showerror
from tkinter import filedialog

# Defining constant
S_HOSTNAME = "localhost"
S_IP = socket.gethostbyname(S_HOSTNAME)
S_PORT = 50000
ACC_SERVER = (S_IP, S_PORT)
MY_PORT = 50001
LISTEN_ADDRESS = ('localhost', MY_PORT)
ENCODER = 'utf-8'
BYTESIZE = 1024

class addfriend_window:
    def __init__(self):
        #define ADD FRIEND window
        self.addfriend_popup = tkinter.Tk()
        self.addfriend_popup.title("Add new friend")
        self.addfriend_popup.geometry("300x160")
        self.addfriend_popup.resizable(0,0)

        #set window colors
        self.addfriend_popup.config(bg=darkgreen)

        #Define GUI Layout
        #Create Frames
        self.input_frame = tkinter.Frame(self.addfriend_popup, bg=white)
        self.output_frame = tkinter.Frame(self.addfriend_popup, bg=darkgreen)

        self.input_frame.pack(pady = 15)
        self.output_frame.pack()

        #Output Frame Layout
        self.result = tkinter.Label(self.output_frame, text = "<result>", font=my_font, fg=white, bg=darkgreen, width= 10)
        self.file_button = tkinter.Button(self.output_frame, text="Send friend request", borderwidth=0, width=15, font=my_font_small, bg=yellow, fg = black, command=lambda: self.get_file())
        self.result.grid(row = 0 , column=0, padx = 5, pady = 5)
        self.file_button.grid(row = 1 , column=0, padx = 5, pady = 5)


        #Input Frame Layout
        self.input_entry = tkinter.Entry(self.input_frame, width=15, borderwidth=0, font=my_font)
        self.search_button = tkinter.Button(self.input_frame, text="Search", borderwidth=0, width=5, font=my_font, bg=yellow, fg = black, command=lambda: self.get_file())
        self.input_entry.grid(row=0, column=0, padx=5, pady=5)
        self.search_button.grid(row=0, column=1, padx=5, pady=5)

    def find_user(self):
        user_id = self.input_entry.get()
        self.server_sock.send(f"FIND {user_id}".encode(ENCODER))
        response = self.server_sock.recv(BYTESIZE).decode(ENCODER)

    def render(self):
        #Run the self.flist_page window's mainloop()
        self.addfriend_popup.mainloop()


test = addfriend_window()
test.render()