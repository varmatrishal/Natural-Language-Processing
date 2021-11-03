from socket import *
from socket import socket
from typing import TextIO


def webservertest():
    serverSocket: socket = socket(AF_INET, SOCK_STREAM)
    serverHost = 'localhost'
    recvBuffer = 1024
    serverPort: int = 80
    serverSocket.bind(('', 80))

    serverSocket.listen(1)
    print("Port Number: ", serverPort)

    while True:
        print("Ready for Server")

        connectionSocket: socket
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024)
            print(message)
            filename = message.split()[1]
            print(filename[1])
            print(filename, "", filename[1])

            f: TextIO = open(filename[1:])
            outputdata = f.read()

            print(outputdata)

            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")

            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i])

            connectionSocket.close()
        except IOError:
            print("404 Not Found")
            connectionSocket.send("""HTTP/1.0 404 Not Found \r\n""".encode());
        finally:
            pass
        break
    pass


if __name__ == "__main__":
    webservertest()
