import socket
import threading


def receive_message():
    while True:
        package = session.recv(1024).decode("utf-8")
        if package:
            print(package)

        elif package == "sair" or package == "exit":
            tcp.close()
            exit(0)

        elif not package:
            pass
    

def send_message():
    while True:
        try:
            msg = str(input("\033[01;32m[SERVIDOR]: \033[0m"))
            session.send(bytes("[SERVIDOR]:" + msg, encoding="utf-8"))
        except:
            print("\033[01;31mErro ao enviar pacote!!\033[0m")
            pass


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 5055
address = (ip, port)

try:
    tcp.bind(address)
    tcp.listen(1)
    print("\033[01;32mServidor em escuta\033[0m")
    print(f"\033[01;32mPorta {port} conectada com sucesso!!\033[0m")
except OSError:
    print("\033[01;31mEssa porta já está em uso\033[0m")
    print("\033[01;31mImpossivel se conectar\033[0m")
    exit(0)

try:
    while True:
        session, client_ip  = tcp.accept()
        if client_ip:
            print(f"\033[01;32m{client_ip[0]} conectado ao servidor\033[0m")

        enviar = threading.Thread(target=send_message, args=())
        enviar.start()
        receber = threading.Thread(target=receive_message, args=())
        receber.start()

except KeyboardInterrupt:
    print("\033[01;31mPrograma Interrompido\033[0m")
