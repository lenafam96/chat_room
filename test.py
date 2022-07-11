from tkinter import *
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.geometry('450x700')
        self.switch_frame(Login)
        # self.switch_frame(MainWindows)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def change_title(self, name):
        self.title(name)


class Login(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        master.change_title('Login')
        Label(self, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n").grid(row=0, column=0)
        Label(self, text="User Name: ").grid(row=1, column=0)
        self.username = StringVar()
        Entry(self, textvariable=self.username).grid(row=1, column=1)
        Label(self, text="").grid(row=2, column=0)
        Label(self, text="Password: ").grid(row=3, column=0)
        self.password = StringVar()
        Entry(self, textvariable=self.password,
              show='*').grid(row=3, column=1)
        Label(self, text="").grid(row=4, column=0)
        Button(self, text="Login", command=self.validateLogin, width=10, height=2).grid(
            row=5, column=1)
        Label(self, text="").grid(row=5, column=0)
        self.message = Label(self, text="")
        self.message.grid(row=6, column=0)

    def validateLogin(self):
        username = self.username.get()
        password = self.password.get()
        print("username entered :", username)
        print("password entered :", password)

        msg = "{};{}".format(username, password)

        client_socket.send(bytes(msg, "utf8"))

        answer = client_socket.recv(
            BUFSIZ).decode("utf8")

        if(answer == 'True'):
            print('correct')
            self.master.switch_frame(MainWindows)
        else:
            print('incorrect')
            self.message.config(text='incorrect')


class MainWindows(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        master.change_title('Phòng chat nhóm 9')
        messages_frame = Frame(master)
        self.my_msg = StringVar()

        self.scrollbar = Scrollbar(messages_frame)

        self.msg_list = Text(messages_frame, height=40,
                             width=70, yscrollcommand=self.scrollbar.set, wrap=WORD, font=("Helvetica", 10))
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.msg_list.pack(side=LEFT, fill=BOTH)
        self.msg_list.pack()
        self.msg_list.bind("<Key>", lambda e: "break")
        messages_frame.pack()

        self.entry_field = Entry(master, textvariable=self.my_msg, width=30)
        self.entry_field.bind("<Return>", self.send)
        self.entry_field.pack()
        self.send_button = Button(
            master, text="Gửi", command=self.send, width=15)
        self.send_button.pack()

        master.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.receive_thread = Thread(target=self.receive)
        self.receive_thread.start()

    def receive(self):
        while True:
            try:
                msg = client_socket.recv(
                    BUFSIZ).decode("utf8")
                self.msg_list.insert(END, msg + "\n")
                self.msg_list.yview(END)
            except OSError:
                break

    def send(self, event=None):
        msg = self.my_msg.get()
        self.my_msg.set("")
        client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            client_socket.close()
            self.master.quit()

    def on_closing(self, event=None):
        self.my_msg.set("{quit}")
        self.send()


if __name__ == "__main__":
    # Kết nối tới server
    HOST = '192.168.1.12'
    PORT = 33000

    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(ADDR)

    app = SampleApp()
    app.mainloop()
