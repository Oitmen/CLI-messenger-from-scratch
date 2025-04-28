# CLI Messenger from Scratch
This is a simple messenger with chatrooms build nearly completly from sratch using Python build with a custom protocl based on tcp

## Goal

A simpel Messenger with chatrooms build to learn new stuff and deepen my knowledge
All writen without Ai.


## Protocol

+ Version(1byte)
+ OPCODES(1byte)
+ Stream(1byte)
+ Leghtn (2byte)
+ Body (Variable)

### OPCODES

+ 0x01 SEND_MESSAGE
+ 0x02 RECEIVE_MESSAGE
+ 0x03 LIST_ROOMS
+ 0x04 JOIN_ROOM
+ 0x05 CREATE_ROOM
+ 0x06 SERVER_MESSAGE
