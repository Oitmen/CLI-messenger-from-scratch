import socket
import threading

host = "127.0.0.1"
port = 8888

rooms = ["main"]

def handler(conn, addr):
    with conn: 
        print(f"connected by {addr}")
        while True:
            sample_data = bytes([0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01])
            conn.sendall(packet("RECEIVE_MESSAGE", sample_data))
            
            
def packet(opcode, body):
    version = 0x01
    OPCODES = {
        "SEND_MESSAGE": 0x01,
        "RECEIVE_MESSAGE": 0x02,
    }
    
    opcode_bin = OPCODES.get(opcode)
    length = len(body).to_bytes(2, "big")
    
    header = bytes([version, opcode_bin]) + length
    packet = header + body
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
            
            
