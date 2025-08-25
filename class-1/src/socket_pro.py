import socket

def tcp_head(host, port=80, path="/"):
    req = f"HEAD {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(3)
        s.connect((host, port))
        s.sendall(req.encode("ascii"))
        data = s.recv(1024)
        return data.decode("latin-1", errors="ignore").split("\r\n")[0]
    
print(tcp_head("https://google.com", 80))