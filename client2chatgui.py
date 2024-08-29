import socket
from threading import Thread

# Setup for client
server_IP = "localhost"
server_Port = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((server_IP, server_Port))
    print("Connected to the server.")
except Exception as e:
    print(f"Failed to connect to the server: {e}")
    exit()

def receiving_msg(connection):
    while True:
        try:
            msg = connection.recv(1024).decode('utf-8')  
             
            if msg:
                print(f"haow oare u : {msg}")  
                if msg == "Can":
                    connection.send("IT IS !@#$%".encode('utf-8')) 


            
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def send_msg(connection, msg_send):
    try:
        connection.send(msg_send.encode('utf-8'))
    except Exception as e:
        print(f"Error sending message: {e}")

# Thread to handle receiving messages
receive_thread = Thread(target=receiving_msg, args=(client,))
receive_thread.start()

# The send function will be called from main.py
