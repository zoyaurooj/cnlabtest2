from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
sentence = input("Enter a word : ")
clientSocket.sendto(bytes(sentence,"utf-8"),(serverName,serverPort))
filecontents,aerverAddress = clientSocket.recvfrom(2048)
print("from server : ",filecontents.decode('utf-8'))
clientSocket.close()
