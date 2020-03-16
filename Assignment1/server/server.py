import socket
from get_student_info import get_student_info

# tao 1 socket  
s = socket.socket()
# cai dat Tai su dung lai port cho socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = socket.gethostname()
port = 1357
# Chi dinh hostname va port cho socket 
s.bind((host, port))

# Doi 5s de ket noi voi client
s.listen(5)

# Khi co client ket noi vao socket thiet lap ket noi va gui data
while True:
    c, addr = s.accept()
    print("da ket noi voi", addr)
    mssv = c.recv(1024).decode('utf8')
    print("Client send student id:", mssv)
    student_info = get_student_info(mssv)
    student_info = str(student_info) if student_info else '{}'
    c.send(student_info.encode())
    c.close()

