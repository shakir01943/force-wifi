import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
h = socket.gethostname()
p = 1230
s.bind((h, p))
s.listen(2)
msg , address = s.accept()
print("connect",address)

def sandmassage():
    m = input("write your massage: ")
    msg.send(m.encode("utf-8"))
def recivemassage():
    ms = s.recv(1234)
    print(ms)

loop = True
while loop:
    if loop == True:
       sandmassage()
       recivemassage()
    else:
        s.close()
        break


