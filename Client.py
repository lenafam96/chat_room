from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *


def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(END, msg)
        except OSError:
            break


def send(event=None):
    msg = my_msg.get()
    my_msg.set("")
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    my_msg.set("{quit}")
    send()


def click(event):
    entry_field.configure(state=NORMAL)
    entry_field.delete(0, END)
    entry_field.unbind('<Button-1>', clicked)


top = Tk()
top.title("Phòng chat nhóm 9")
top.geometry('450x700')

messages_frame = Frame(top)
my_msg = StringVar()
my_msg.set("Nhập tên của bạn!") 

scrollbar = Scrollbar(messages_frame)

msg_list = Listbox(messages_frame, height=40,
                   width=70, yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = Entry(top, textvariable=my_msg, width=30)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = Button(top, text="Gửi", command=send, width=15)
send_button.pack()

clicked = entry_field.bind('<Button-1>', click)

top.protocol("WM_DELETE_WINDOW", on_closing)

# Kết nối tới server
HOST = '127.0.0.1'
PORT = 33000

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
mainloop()
