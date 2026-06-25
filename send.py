import socket

# UDP Socket create karein
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Socket ko broadcast permission dein
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

message = input("Enter your Message :- ")

# 255.255.255.255 broadcast address hai, jo network ke har device ko message bhejega
sock.sendto(message.encode('utf-8'), ('255.255.255.255', 8080))

print("Broadcast message sent successfully!")
