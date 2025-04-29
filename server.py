import socket
import threading
from protocol import create_packet
host = "127.0.0.1"
port = 8888

rooms = ["main", "game"]

def handler(conn, addr):
    try:
        with conn: 
            print(f"connected by {addr}")
            while True:
                data = conn.recv(4048)
                OPCODES = {
                    0x01: "SEND_MESSAGE",
                    0x02: "RECEIVE_MESSAGE",
                    0x03: "LIST_ROOMS",
                    0x04: "JOIN_ROOM",
                    0x05: "CREATE_ROOM",
                    0x06: "SERVER_MESSAGE"
                }
                
                opcode = OPCODES.get(data[1])
                
                if opcode == "LIST_ROOMS":
                    print("Requested list of Rooms")
                    for i in range(len(rooms)):
                        print(rooms[i])
                        if i == 0:
                            conn.sendall(create_packet("SERVER_MESSAGE", 0x01, 0x01, rooms[i]))
                        elif i == len(rooms) - 1:
                            conn.sendall(create_packet("SERVER_MESSAGE", 0x01, 0x02, rooms[i]))
                        else:
                            conn.sendall(create_packet("SERVER_MESSAGE", 0x01, 0x00, rooms[i]))
    finally:
        conn.close()
                    

    
            
            
            
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("server lisening")
        try:
            while True:            
                conn, addr = s.accept()
                threading.Thread(target=handler, args=(conn, addr), daemon=True).start()
        except KeyboardInterrupt:
            print("Server shutting down")
            
            
