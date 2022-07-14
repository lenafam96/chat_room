from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import mysql.connector
from datetime import datetime

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="roomchat"
# )

try:
    mydb = mysql.connector.connect(
        host="sql6.freesqldatabase.com",
        user="sql6505713",
        password="MDkCNzPSum",
        database="sql6505713"
    )
except:
    print("Lỗi kết nối!")


def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        print(dt_string + ": %s:%s has connected." % client_address)
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    auth = False
    username = ""
    while not auth:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8") and msg != bytes("", "utf8"):
            login = msg.decode("utf8").split(';')
            username = login[0]

            auth = authentication(login[0], login[1])
            client.send(bytes(str(auth), "utf8"))
        else:
            client.close()
            break
    load_old_message(client)
    welcome = 'Xin chào %s! Nếu bạn muốn thoát gõ, {quit} để thoát.' % username
    client.send(bytes(welcome, "utf8"))
    msg = "%s đã tham gia phòng chat!" % username
    broadcast(bytes(msg, "utf8"))
    clients[client] = username

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            insert_message(username, msg)
            broadcast(msg, username + ": ")
        else:
            client.close()
            del clients[client]
            broadcast(bytes("%s đã thoát phòng chat." % username, "utf8"))
            break


def broadcast(msg, prefix=""):
    if len(clients) > 0:
        for sock in clients:
            sock.send(bytes(prefix, "utf8") + msg)


def authentication(username, password):
    mycursor = mydb.cursor()

    mycursor.execute(
        "SELECT * FROM `user` where username = '{}' and password = '{}'".format(username, password))

    myresult = mycursor.fetchall()

    return True if len(myresult) > 0 else False


def insert_message(username, msg):
    now = datetime.now()

    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

    mycursor = mydb.cursor()

    sql = "INSERT INTO `message` (username, time, content) VALUES (%s,%s,%s)"
    val = (username, dt_string, msg)

    mycursor.execute(sql, val)

    mydb.commit()


def load_old_message(client):
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT * FROM(SELECT * FROM `message` ORDER BY message_id DESC LIMIT 50) as LIST ORDER BY message_id ASC")

    myresult = mycursor.fetchall()
    client.send(bytes("Tin nhắn cũ\n.....", "utf8"))
    for x in myresult:
        client.send(bytes("{} ({}): {}\n".format(x[1], x[2], x[3]), "utf8"))

    client.send(
        bytes("-----------------------------------------------------\n", "utf8"))


clients = {}
addresses = {}

HOST = '103.166.185.209'
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Chờ kết nối từ các client...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
