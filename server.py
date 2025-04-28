import socket
import threading

host = "127.0.0.1"
port = 8888

def handler(conn, addr):
    with conn: 
        print(f"connected by {addr}")
        while True:
            data = conn.recv(1024)
            print(data)
            conn.sendall(data)
            
            
            
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("server lisening")
        while True:            
            conn, addr = s.accept()
            threading.Thread(target=handler, args=(conn, addr), daemon=True).start()
            
