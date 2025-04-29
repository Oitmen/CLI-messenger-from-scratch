def create_packet(opcode,stream, flag, body):
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
    
    header = bytes([version, opcode_bin, stream, flag]) + length
    packet = header + body.encode('utf-8')
    return packet

def get_body(data):
    length_bytes = data[4:6]
    legnth = int.from_bytes(length_bytes, "big")
    
    body_bytes = data[6:6+legnth]
    return body_bytes.decode("utf-8")

 