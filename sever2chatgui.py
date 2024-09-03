import socket
import threading
import sys
import time
def create_socket():
    global host, port, s
    try:
        host = "localhost"  # Bind to all available network interfaces
        port = 9999
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
        print("Socket created")
    except socket.error as msg:
        print("Socket creation error:", msg)
        sys.exit()

def bind_socket():
    global s
    while True:
        try:
            print("Binding the port", port)
            s.bind((host, port))  # Bind to the host and port
            s.listen(5)  # Listen for up to 5 incoming connections
            print("Socket listening on port", port)
            break
        except socket.error as msg:
            print("Socket binding error:", msg)
            print("Retrying in 5 seconds...")
            time.sleep(5)  # Wait before retrying

def socket_accept():
    while True:
        try:
            conn, address = s.accept()  # Accept a connection
            print(f"Connected to {address[0]}:{address[1]}")

            # Create threads for sending and receiving messages
            threading.Thread(target=send_commands, args=(conn,)).start()
            threading.Thread(target=receive_commands, args=(conn,)).start()
        except Exception as e:
            print(f"Error accepting connection: {e}")

def send_commands(conn):
    while True:
        try:
            cmd = input("Enter command Message for Client: ")
            conn.send(cmd.encode('utf-8'))
        except Exception as e:
            print(f"Error sending command: {e}")
            conn.close()  # Close the connection on error
            break

def receive_commands(conn):
    while True:
        try:
            client_response = conn.recv(1024).decode("utf-8")  # Receive response from the client
            print(client_response)
            if client_response:
                print(f"Client: {client_response}")  # Debugging line

                if client_response == "send_deets":
                    file_path = "File-forcarpark.txt"
                    
                    try:
                        with open(file_path, 'r') as file:
                            while True:
                                chunk = file.read(1024)  # Read the file in chunks
                                if not chunk:
                                    break
                                conn.send(chunk.encode('utf-8'))  # Send chunk to client
                        conn.send(b"EOF")  # Send end-of-file signal
                    except FileNotFoundError:
                        print("File not found.")
                        conn.send(b"File not found.")
                    
                elif client_response == "Content":
                    can = "Can"
                    conn.send(can.encode("utf-8"))
                    content = conn.recv(1024).decode("utf-8")

                    
                    
                    
                
                 
                

        except Exception as e:
            print(f"Error receiving response: {e}")
            break
    
    conn.close()  # Ensure the connection is closed
  # Ensure the connection is closed

def main():
    create_socket()  # Create the socket
    bind_socket()  # Bind the socket to the address and port
    socket_accept()  # Accept and handle incoming connections

if __name__ == "__main__":
    main()
