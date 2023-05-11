# Client Chat App
import tkinter, socket, threading, os
from tkinter import *
from tkinter import messagebox
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
        self.signin_button = tkinter.Button(self.login_frame, text="Sign in", font=my_font, fg = black, bg=yellow, borderwidth=0, width=10, height=3, command = lambda: self.check_fields())
        self.register_button = tkinter.Button(self.login_frame, text="Register", font=my_font_small, fg = white, bg=lightgreen, borderwidth=0, width=8, command = lambda: self.register())
        self.forgotpw_button = tkinter.Button(self.login_frame, text="Forgot password", font=my_font_small, fg = white, bg=lightgreen, borderwidth=0, width= 16, command=lambda: self.forgot_password())
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

    def check_fields(self):
        if self.uid_entry.get() == "" or self.pw_entry == "":
            self.pop_up("Missing field(s)!", "Please fill in every field(s)!")
        else:
            self.login()

    def login(self):
        #global myID, password, friend_list, server_sock, login_win, friendlist_win
        myID = self.uid_entry.get()
        password = self.pw_entry.get()
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server_sock.connect(ACC_SERVER)
        except:
            messagebox.showerror("Connect failed!", "Cannot connect to the server!")
            return
        server_sock.send(f"LOGIN {myID}_{password}".encode(ENCODER))
        response = server_sock.recv(BYTESIZE).decode(ENCODER)
        if (response == "FAIL"):
            messagebox.showwarning("Login failed!", "Incorrect User ID or Password!")
        else:
            email = server_sock.recv(BYTESIZE).decode(ENCODER)
            friend_name = server_sock.recv(BYTESIZE).decode(ENCODER).split(' ')
            friend_ip = server_sock.recv(BYTESIZE).decode(ENCODER).split(' ')
            friend_port = server_sock.recv(BYTESIZE).decode(ENCODER).split(' ')
            friend_list = {}
            for i in range(len(friend_name)):
                friend_list[friend_name[i]] = (friend_ip[i], friend_port[i])
            frlist_window(myID, password, email, friend_list, server_sock)
            self.close()

    def register(self):
        pass

    def forgot_password(self):
        pass

    def close(self):
        self.login_page.quit()

    def render(self):
        self.login_page.mainloop()


class frlist_window:
    def __init__(self, myID: str, password: str, email: str, friend_list: dict, server_sock: socket):
        self.myID = myID
        self.password = password
        self.email = email
        self.friend_list = friend_list
        self.server_sock = server_sock
        self.conversation_list = dict
        self.friend_request = []
        
        #Separate friend into online and offline list
        self.onlinelist = []
        self.offlinelist = []
        for userid in self.friend_list:
            if friend_list[userid] == ('NULL', 'NULL'):
                self.offlinelist.append(userid)
            else:
                self.onlinelist.append(userid)
        
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
        self.name = tkinter.Label(self.info_frame, text = self.myID, font=my_font, fg=darkgreen, bg=yellow, width=44, anchor = "nw")
        self.mail_label = tkinter.Label(self.info_frame, text = "User Email:", font=my_font, fg=darkgreen, bg=yellow, width= 10, anchor = "nw")
        self.mail = tkinter.Label(self.info_frame, text = self.email, font=my_font, fg=darkgreen, bg=yellow, width=44, anchor = "nw")

        self.name_label.grid(row = 0 , column=0, padx = 5, pady = 5)
        self.name.grid(row = 0 , column=1, columnspan= 2, padx = 5, pady = 5)
        self.mail_label.grid(row = 1 , column=0, padx = 5, pady = 5)
        self.mail.grid(row = 1 , column=1, columnspan= 2, padx = 5, pady = 5)

        #Label Frame Layout
        self.friend_list_label = tkinter.Label(self.label_frame, text = "Friend List", font=('haveltica', 18), fg=white, bg=darkgreen, width= 30, anchor = "nw")
        self.frrequest_button = tkinter.Button(self.label_frame, text = "Friend request", borderwidth = 0, width = 10, font = my_font_small, bg = yellow, fg = black, command = lambda: self.show_friend_request())
        self.addfr_button = tkinter.Button(self.label_frame, text = "Add friend", borderwidth = 0, width = 10, font = my_font_small, bg = yellow, fg = black, command = lambda: self.add_friend())
        self.friend_list_label.grid(row = 0 , column=0, padx = 5, pady = 5)
        self.frrequest_button.grid(row = 0 , column=1, padx = 5, pady = 5)
        self.addfr_button.grid(row = 0 , column=2, padx = 5, pady = 5)

        #List Frame Layout
        self.my_scrollbar = tkinter.Scrollbar(self.list_frame, orient=VERTICAL)
        self.my_listbox = tkinter.Listbox(self.list_frame, height=20, width=55, borderwidth=0, bg=white, fg=darkgreen, font=my_font, yscrollcommand=self.my_scrollbar.set, selectmode=SINGLE)
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
        self.unfriend_button = tkinter.Button(self.button_frame, text = "Unfriend", width=27, borderwidth = 0, font = my_font, bg = yellow, fg = black, command = lambda: self.unfriend())
        self.chat_button = tkinter.Button(self.button_frame, text = "Start chatting", width = 27, borderwidth = 0, font = my_font, bg = yellow, fg = black, command = lambda: self.start_conversation())
        self.unfriend_button.grid(row=0, column=0,padx=5, pady=5)
        self.chat_button.grid(row=0, column=1, padx=5, pady=5)
        self.update_displaylist(self.onlinelist, self.offlinelist)

        #Pop up confirm message when quit
        self.flist_page.protocol("WM_DELETE_WINDOW", self.close_confirm)

        #Create a thread for listening incoming update from server
        update_thread = threading.Thread(target = self.listen_server)
        update_thread.start()
        
        #Create a thread for listening to friend connections
        connections_thread = threading.Thread(target=self.listen_to_friend)
        connections_thread.start()

    def search_check(self, event):
        typed = self.input_entry.get()
        if typed == '':
            self.update_displaylist(self.onlinelist, self.offlinelist)
        else:
            online_tmplist = []
            offline_tmplist = []
            for user in  self.onlinelist:
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

    def start_conversation(self):
        chosen = self.my_listbox.curselection()
        if len(chosen) == 0:
            showerror(title="No friend selected!", message=f"Please choose a firend to start chatting!")
        else:
            friend_ID = self.my_listbox.get(chosen[0])
            self.connect_to_friend(friend_ID)

    def listen_server(self):
        while True:
            try:
                server_mess = self.server_sock.recv(BYTESIZE).decode(ENCODER)
                if (server_mess == "FRIEND_LIST_UPDATE"):
                    self.frlist_update()
                elif (server_mess == "FRIEND_REQUEST"):
                    user_ID = self.server_sock.recv(BYTESIZE).decode(ENCODER)
                    if user_ID not in self.friend_request:
                        self.friend_request.append(user_ID)
                elif (server_mess == "REQUEST_TIMEOUT"):
                    user_ID = self.server_sock.recv(BYTESIZE).decode(ENCODER)
                    messagebox.showinfo("Friend request timeout!", f"Friend request to {user_ID} has timed out!")
                elif (server_mess == "REQUEST_DENIED"):
                    user_ID = self.server_sock.recv(BYTESIZE).decode(ENCODER)
                    messagebox.showinfo("Friend request denied!", f"Friend request to {user_ID} has been denied!")
                elif (server_mess == "DEL_TIMEOUT_REQUEST"):
                    user_ID = self.server_sock.recv(BYTESIZE).decode(ENCODER)
                    if user_ID in self.friend_request:
                        self.friend_request.remove(user_ID)

            except:
                showerror(title="Server connection lost!", message=f"Cannot connect to server!")
                self.server_sock.close()
                break

    def frlist_update(self):
        #global friend_list, server_sock
        friend_name = self.server_sock.recv(BYTESIZE).decode(ENCODER).split(' ')
        friend_ip = self.server_sock.recv(BYTESIZE).decode(ENCODER).split(' ')
        friend_port = self.server_sock.recv(BYTESIZE).decode(ENCODER).split(' ')
        for i in range(len(friend_name)):
            self.friend_list[friend_name[i]] = (friend_ip[i], friend_port[i])

    def listen_to_friend(self):
        #global listen_sock, conver_win_list
        listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_sock.bind(LISTEN_ADDRESS)
        listen_sock.listen()

        # Verify and Accept or Deny Connection
        while True:
            connected_client, address = listen_sock.accept()
            connected_ID = self.check_address(address)
            if (connected_ID != "NULL"):
                #print("Connected with {}".format(str(address)))
                self.conversation_list[connected_ID] = conversation_window(self.flist_page, self.myID, self.email, connected_ID, connected_client)
            else:
                connected_client.close()

    def connect_to_friend(self, friend_ID):
        #global sock_list
        if friend_ID not in self.conversation_list:
            new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            new_socket.connect(self.friend_list[friend_ID])
            self.conversation_list[friend_ID] = conversation_window(self.flist_page, self.myID, self.email, friend_ID, new_socket)
        else:
            self.conversation_list[friend_ID].bring_to_front()

    def check_address(self, address):
        for userid in self.friend_list:
            if self.friend_list[userid] == address:
                return userid
        return "NULL"

    def add_friend(self):
        addFriend_window()
    
    def unfriend(self):
        chosen = self.my_listbox.curselection()
        if len(chosen) == 0:
            showerror(title="No friend selected!", message=f"Please choose a firend to start chatting!")
        else:
            friend_ID = self.my_listbox.get(chosen[0])
            self.server_sock.send(f"UNFRIEND {friend_ID}".encode(ENCODER))
    
    def show_friend_request(self):
        pass

    def create_chatroom(self):
        pass

    def close_confirm(self):
        confirm_reply = askyesno(title="Log out?", message="You will log out this user once you close this window!\nDo you want to log out?")
        if confirm_reply:
            for friend in self.conversation_list:
                self.conversation_list[friend].disconnect()
                self.conversation_list.pop(friend)
            self.flist_page.destroy()
            login_window()


class conversation_window:
    def __init__(self, root: Tk, myID: str, email: str, userid: str, user_socket: socket):
        self.userid = userid
        self.user_socket = user_socket

        #define CONVERSATION window
        self.conver_page = tkinter.Toplevel(root)
        self.conver_page.title(f"Simple P2P Chat application - Conversation with {self.userid}")
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
        self.name = tkinter.Label(self.info_frame, text = myID, font=my_font, fg=darkgreen, bg=yellow, width=44, anchor = "nw")
        self.mail_label = tkinter.Label(self.info_frame, text = "User Email:", font=my_font, fg=darkgreen, bg=yellow, width= 10, anchor = "nw")
        self.mail = tkinter.Label(self.info_frame, text = email, font=my_font, fg=darkgreen, bg=yellow, width=44, anchor = "nw")

        self.name_label.grid(row = 0 , column=0, padx = 5, pady = 5)
        self.name.grid(row = 0 , column=1, columnspan= 2, padx = 5, pady = 5)
        self.mail_label.grid(row = 1 , column=0, padx = 5, pady = 5)
        self.mail.grid(row = 1 , column=1, columnspan= 2, padx = 5, pady = 5)

        self.friend_list_label = tkinter.Label(self.label_frame , text = f"Chatting with {self.userid}", font=('haveltica', 18), fg=white, bg=darkgreen, width=44, anchor = "nw")
        self.friend_list_label.grid(row = 0 , column=0, padx = 5, pady = 5)

        #Output Frame Layout
        self.my_scrollbar = tkinter.Scrollbar(self.output_frame, orient=VERTICAL)
        self.my_listbox = tkinter.Listbox(self.output_frame, height=20, width=55, borderwidth=0, bg=white, fg=darkgreen, font=my_font, yscrollcommand=self.my_scrollbar.set)
        self.my_scrollbar.config(command=self.my_listbox.yview)
        self.my_listbox.grid(row=0, column=0)
        self.my_scrollbar.grid(row=0, column=1, sticky="NS")

        #Input Frame Layout
        self.input_entry = tkinter.Entry(self.input_frame, width=39, borderwidth=0, font=my_font)
        self.file_button = tkinter.Button(self.input_frame, text="File", borderwidth=0, width=7, font=my_font, bg=yellow, fg = black, command = lambda: self.send_file())
        self.send_button = tkinter.Button(self.input_frame, text="Send", borderwidth=0, width=7, font=my_font, bg=yellow, fg = black, command = lambda: self.send_message())
        self.input_entry.grid(row=0, column=0, padx=5, pady=5)
        self.file_button.grid(row=0, column=1, padx=5, pady=5)
        self.send_button.grid(row=0, column=2, padx=5, pady=5)

        #Pop up confirm message when quit
        self.conver_page.protocol("WM_DELETE_WINDOW", self.close_confirm)

        #Create a thread for listening incomming messages
        self.receive_thread = threading.Thread(target=self.recieve_message)
        self.receive_thread.start()

    def add_to_list(self, message):
        self.my_listbox.insert(END, message)

    def disconnect(self):
        self.user_socket.close()
        self.conver_page.destroy()

    def send_message(self):
        message = self.input_entry.get()
        check_mess = []
        for index in range(6):
            check_mess[index] = message[index] 
        if check_mess == "<FILE>":
            showerror(title="Message syntax error!", message="Please do not start a message with FILE: '!")
        else:
            self.user_socket.send(f"m {message}".encode(ENCODER))
            self.add_to_list(f"You: {message}")

    def send_file(self):
        file_path = self.get_file()
        file_name = os.path.basename(file_path)
        file = open(file_path, 'rb')
        file_size = os.path.getsize(file_path)
        self.user_socket.send(f"f {file_name}:{str(file_size)}".encode(ENCODER))
        data = file.read()
        self.user_socket.sendall(data)
        self.user_socket.send(b"<END_FILE>")
        self.add_to_list(END, f"<FILE>You: {file_name}")
        self.my_listbox.itemconfig(END,{'fg':'blue'})
        #self.my_listbox.itemconfig(END,{'font: my_font_italic_underscore'})
        file.close()

    def recieve_message(self):
        while True:
            try:
                type, message = self.user_socket.recv(BYTESIZE).decode(ENCODER).split(' ')
                if (type == 'm'):
                    message = '{}: {}'.format(self.userid, message)
                    self.add_to_list(message)
                else:
                    file_name = message.split(':')
                    file_path = f"/{self.userid}/file/{file_name}"
                    is_existed = os.path.isfile(file_path)
                    i = 1
                    while is_existed:
                        file_path = f"/{self.userid}/file/{file_name}_({str(i)})"
                        is_existed = os.path.isfile(file_path)
                        i += 1
                
                    file = open(file_path, 'wb')
                    file_bytes = b""
                    done = False

                    while not done:
                        file_data = self.user_socket.recv(1024)
                        file_bytes += file_data
                        if file_bytes[-10:] == b"<END_FILE>":
                            done = True
                            file_bytes -= b"<END_FILE>"

                    file.write(file_bytes)
                    file.close()
                    message = '<FILE>{}: {}'.format(self.userid, file_name)
            except:
                #An error occured, disconnect from the server
                #conver_win_list.pop(self.userid)
                #sock_list.pop(self.userid)
                showerror(title="Connection lost!", message=f"{self.userid} has left the conversation!")
                self.user_socket.close()
                break

    def close_confirm(self):
        confirm_reply = askyesno(title="Leave conversation?", message="You will disconnect with this user and the conversation will be deleted when you close this window!\nDo you want to leave?")
        if confirm_reply:
            self.user_socket.close()
            self.conver_page.destroy()

    def get_file(self):
        filename = filedialog.askopenfilename(title='Select a file')
        #tkinter.Label(tkinter.Toplevel(), text = self.filename).pack()
        return filename

    def bring_to_front(self):
        self.conver_page.lift()

class addFriend_window:
    def __init__(self, root: Tk, server_sock: socket):
        self.server_sock = server_sock
        
        #define ADD FRIEND window
        self.addfriend_popup = tkinter.Toplevel(root)
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
        self.add_button = tkinter.Button(self.output_frame, text="Send friend request", borderwidth=0, width=15, font=my_font_small, bg=yellow, fg = black, state=DISABLED, command=lambda: self.request_friend())
        self.result.grid(row = 0 , column=0, padx = 5, pady = 5)
        self.add_button.grid(row = 1 , column=0, padx = 5, pady = 5)


        #Input Frame Layout
        self.input_entry = tkinter.Entry(self.input_frame, width=15, borderwidth=0, font=my_font)
        self.search_button = tkinter.Button(self.input_frame, text="Search", borderwidth=0, width=5, font=my_font, bg=yellow, fg = black, command=lambda: self.find_user())
        self.input_entry.grid(row=0, column=0, padx=5, pady=5)
        self.search_button.grid(row=0, column=1, padx=5, pady=5)

    def find_user(self):
        user_id = self.input_entry.get()
        self.server_sock.send(f"FIND {user_id}".encode(ENCODER))
        response = self.server_sock.recv(BYTESIZE).decode(ENCODER)
        if response == "FOUND_ONLINE":
            self.result.config(text = f"{user_id} is online")
            self.add_button.config(state= NORMAL)
        elif response == "FOUND_OFFLINE":
            self.result.config(text = f"{user_id} is offline")
        else:
            self.result.config(text = "Not found!")

    def request_friend(self):
        self.add_button.config(state= DISABLED)
        user_id = self.result.cget('text')
        self.server_sock.send(f"REQUEST {user_id}".encode(ENCODER))

class register_window:
    pass

class forgotPassword_window:
    pass

class friendRequest_window:
    pass

class chatroom_window:
    pass

login_window().render()

