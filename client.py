import socket
import threading


def receive_message():
    while True:
        package = tcp.recv(1024).decode("utf-8")
        if package:
            print(package)

        elif package == "sair" or package == "exit":
            tcp.close()
            exit(0)
        
        elif not package:
            continue
    

def send_message():
    while True:
        try:
            msg = str(input(f"\033[01;32m[{nome}]: \033[0m"))
            msg = (f"[{nome}]:" + msg)
            tcp.send(bytes(msg, encoding="utf-8"))
        except:
            print("\033[01;31mErro ao enviar pacote!!\033[0m")
            continue


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 5055
address = (ip, port)

try:
    tcp.connect(address)
    print(f"\033[01;32mConectado ao servidor\033[0m")
    print("\033[01;33mDigite seu nome\033[0m")
    nome = str(input("==> ")).lower()
except:
    print("\033[01;31mFalha ao se conectar\033[0m")
    exit(0)

enviar = threading.Thread(target=send_message, args=())
enviar.start()

receber = threading.Thread(target=receive_message, args=())
receber.start()