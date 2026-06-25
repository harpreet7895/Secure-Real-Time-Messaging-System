import socket

# UDP Socket create karein
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Sabhi network interfaces ke port 8080 par bind karein
sock.bind(("", 8080))

print("Laptop is listening for broadcast messages on port 8080...")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received from {addr}: {data.decode('utf-8')}")
