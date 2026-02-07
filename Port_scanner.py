import socket

target = "127.0.0.1"

ports = [21,22,23,25,80,443]
for PORT in ports:
    s = socket.socket()
    s.settimeout(0.5)
    
    result = s.connect_ex((target, PORT))
    
    if result == 0:
        print(f"Port {PORT} is open")
        
    else:
        print(f"Port {PORT} is not open")
        
    s.close()
