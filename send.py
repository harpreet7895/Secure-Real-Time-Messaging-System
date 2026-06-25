import socket

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enable broadcast mode on the socket
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

message = input("Enter your Message :- ")

# 255.255.255.255 is a broadcast address that sends the message to every device on the network.
sock.sendto(message.encode('utf-8'), ('255.255.255.255', 8080))

print("Broadcast message sent successfully!")
