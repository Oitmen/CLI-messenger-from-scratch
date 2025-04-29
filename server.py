import socket
import threading

host = "127.0.0.1"
port = 8888

rooms = ["main", "game"]

def handler(conn, addr):
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
            
            if(opcode == "LIST_ROOMS"):
                print("Requested list of Rooms")
                for room in rooms:
                    print(room)
                    conn.sendall(create_packet("SERVER_MESSAGE", room))             
            # sample_data = bytes([0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01])
           #  conn.sendall(packet("RECEIVE_MESSAGE", sample_data))
            
            
def create_packet(opcode, body):
    body_binary = ''.join(format(ord(char), '08b') for char in body)
    
    version = 0x01
    OPCODES = {
        "SEND_MESSAGE": 0x01,
        "RECEIVE_MESSAGE": 0x02,
        "LIST_ROOMS": 0x03,
        "JOIN_ROOM": 0x04,
        "CREATE_ROOM": 0x05,
        "SERVER_MESSAGE": 0x06
    }
    
    opcode_bin = OPCODES.get(opcode)
    length = len(body).to_bytes(2, "big")
    
    header = bytes([version, opcode_bin]) + length
    packet = header + body.encode('utf-8')
    return packet

 
    
            
            
            
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
            
            
