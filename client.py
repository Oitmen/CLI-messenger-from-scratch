import socket
from protocol import create_packet, get_body

HOST = "127.0.0.1"  
PORT = 8888


            

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(create_packet("LIST_ROOMS",0x01, 0x03, "0"))
    stream_open = True
    while stream_open:
        data = s.recv(10024)
        if(data[3] == 0x02): stream_open = False
        print(get_body(data))
    uinputr = input("Which Room do you want to Join?")
    s.sendall(create_packet("JOIN_ROOM",0x01,0x03,uinputr))
    
    
        