import socket
import threading
from protocol import create_packet, get_body
host = "127.0.0.1"
port = 8888

rooms = {"main": [], "game": []}


def handler(conn, addr):
    try:
        with conn: 
            print(f"connected by {addr}")
            print(conn)
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
                    room_names = list(rooms.keys())
                    for i, room in enumerate(room_names):
                        print(room)
                        flag = 0x00
                        if i == 0:
                            flag = 0x01
                        elif i == len(room_names) - 1:
                            flag = 0x02
                        conn.sendall(create_packet("SERVER_MESSAGE", 0x01, flag, room))
                elif (opcode == "JOIN_ROOM"):
                    rooms[get_body(data)].append(addr)
                    print(rooms)
                    
                    
    finally:
        for room in rooms.values():
            if addr in room:
                room.remove(addr)
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
            
            
