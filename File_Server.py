import socket
import threading
import hashlib
import sys

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 8081
bufsize = 1073741824
serversock.bind((host,port))
path = "/var/www/html/videos"
filename = ""
serversock.listen(10)
while True:
    print ("Waiting for a connection.....")

    clientsocket,addr = serversock.accept()
    print("Got a connection from %s" % str(addr))
    try:
        while(True):
            filename = clientsocket.recv(1024)
            clientsocket.send(bytes('Name_recv'))
            #filesize = clientsocket.recv(32)
            #print(filesize)
            #filesize = int(filesize, 2)
            if(filename.decode() != "Done"):
                print(filename.split())
                print(filename)
                print(filename.decode())
                size = clientsocket.recv(1024)
                size = int(size.decode())
                clientsocket.send(bytes("Size_recv"))
                data = b""
                while(True):
                    datum = clientsocket.recv(bufsize)
                    size -= len(datum)
                    data += datum
                    if size <= 0 : break
                    print('writing file .... %d' % size)
        
                file_to_write = open(path + filename.decode(), 'wb')
                file_to_write.write(data)
                file_to_write.close()
                print('File received successfully')
                clientsocket.send(bytes('Good'))
            else:
                print("Finished connection with %s" % str(addr))
                break;
    except:
        print("Unexpected error:", sys.exc_info()[0])
        print("Connection lost with %s" % str(addr))
    #size = clientsocket.recv(1024) # Note that you limit your filename length to 255 bytes.
    #if not size:
     #   break
    #size = format(size,'b')
    #print(size)
    #size = int(size, 2)
        #chunksize = 4096
        ##chunks = []
##        while(True):
##            print("recv")
##            chunk = clientsocket.recv(4096)
##            print("Did recv")
##            try:
##                V = chunk.split()
##                S = ""+V[-3].decode()+" "+V[-2].decode()+" "+V[-1].decode()
##                print(chunk)
##                print(S)
##                if(S == 'Finished sendding file'):
##                    CH = b''.join(V[:-3])
##                    chunks.append(CH)
##                    break
##            except(UnicodeDecodeError):
##                chunks.append(chunk)
##        file_to_write.write(b''.join(chunks))
##    while filesize > 0:
##        if filesize < chunksize:
##            chunksize = filesize
##        data = clientsocket.recv(chunksize)
##        file_to_write.write(data)
##        filesize -= chunksize
    
serversock.close()
