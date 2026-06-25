# Secure Real Time Messaging System
python based real-time messaging system for secure communication over a Local Area Network 

## Project Overview

This project is a Python-based secure messaging application that enables real-time communication between users over a Local Area Network (LAN). The sender can send messages instantly, and the receiver receives them without delay.

## Features

* Real-time message transmission
* Instant message delivery
* Client-Server architecture
* Communication over LAN
* Easy-to-use interface
* Lightweight and efficient

## Technologies Used

* Python
* Socket Programming
* TCP/IP Protocol
* Networking Concepts

## Working

1. The server starts and waits for incoming connections.
2. The client connects to the server using the server IP address.
3. The sender enters a message.
4. The message is transmitted through the network.
5. The receiver instantly receives and displays the message.
6. Both devices must be connected to the same Wi-Fi/LAN network. 

## Project Structure

```
project/
│
├── send.py
├── rec.py
├── README.md
└── requirements.txt
```

## How to Run

### Start the Server

```bash
python send.py
```

### Start the Client

```bash
python rec.py
```
## Example 

Laptop A (Sender)  -> "Hello everyone"           |   |                    
   Laptop B (rec.py running)                 Laptop C (rec.py running) 

Output on both : Hello everyone

## Future Enhancements

* End-to-End Encryption
* User Authentication
* File Sharing
* Group Chat
* Message Logging
* GUI Interface

## Author

Harpreet Kaur
