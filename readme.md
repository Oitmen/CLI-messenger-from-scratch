# CLI Messenger from Scratch

## What is this?
- Simple CLI-based messenger with room functionality
- Built completely from scratch using Python and TCP sockets
- Custom binary protocol for network communication
- Supports multiple chatrooms
- Multi-user support through concurrent connections

## What I learned from this project
- Socket programming and TCP/IP networking
- Binary protocol design and implementation
- Concurrent programming with threads
- Client-server architecture patterns
- Low-level packet structure and parsing
- Room-based message broadcasting
- Error handling in distributed systems

## Protocol Packet Structure
```
+----------------+----------------+----------------+----------------+----------------+----------------+
| Version (1B)   | OPCODE (1B)   | Stream (1B)   | Flag (1B)     | Length (2B)   | Body (VarLen) |
+----------------+----------------+----------------+----------------+----------------+----------------+
```

## OPCODES
- 0x01: SEND_MESSAGE
- 0x02: RECEIVE_MESSAGE
- 0x03: LIST_ROOMS
- 0x04: JOIN_ROOM
- 0x05: CREATE_ROOM
- 0x06: SERVER_MESSAGE

## Stream Values
- 0x01: SYSTEM
- 0x02-0x09: Reserved for future special rooms
- 0x0A-0xFF: Room IDs

## Flags
- 0x01: START_OF_STREAM
- 0x02: END_OF_STREAM
- 0x03: SINGLE_MESSAGE
