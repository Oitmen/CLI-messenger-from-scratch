import socket

HOST = "127.0.0.1"  
PORT = 8888


            
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
    s.connect((HOST, PORT))
    s.sendall(create_packet("LIST_ROOMS", "0"))
    while True:
        data = s.recv(10024)
        print(data)
        if len(data) >= 4:
            version = data[0]
            opcode = data[1]
            length = int.from_bytes(data[2:4], "big")
            body = data[4:4+length].decode('utf-8')
        
            print(f"Version: {version}, Opcode: {opcode}, Length: {length}")
            print(f"Body: {body}") 