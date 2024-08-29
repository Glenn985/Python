from client2chatgui import send_msg, client
from threading import Thread

def main():
    # Thread to handle sending messages
    def handle_sending():
        while True:
            msg_send = input("Send message: ")
            send_msg(client, msg_send) 

    # Start the sending thread
    send_thread = Thread(target=handle_sending)
    send_thread.start()
    
    # Join threads to ensure they complete (optional, depending on your needs)
    send_thread.join()

if __name__ == "__main__":
    main()



