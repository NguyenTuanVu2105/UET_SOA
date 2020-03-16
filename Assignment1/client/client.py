import socket 

# Tao 1 socket 
s = socket.socket()
host = socket.gethostname()
port = 1357

mssv = input("Nhap mssv:")
# Ket noi voi socket phia server
s.connect((host, port))
# Gui va nhan data. Vi khong gui duoc dang string nen p encoding de chuyen sang dang byte
s.send(mssv.strip().encode())
print(s.recv(1024).decode('utf8'))
s.close()