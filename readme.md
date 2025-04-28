# CLI Messenger from Scratch
This is a simple messenger with chatrooms build nearly completly from sratch using Python build with a custom protocl based on tcp

## Protocol

+ Version(1byte)
+ OPCODES(1byte)
+ Stream(1byte)
+ Leghtn (2byte)
+ Body (Variable)

### OPCODES

+ 0x01 Send_Message
+ 0x02 Recive_Message
+ 0x03
