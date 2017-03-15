import socket,os,threading

def File_Send():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "172.113.170.244"
#    host = "127.0.0.1"
    port = 8081
    s.connect((host, port))
    path = "/var/www/html/videos"
    directory = os.listdir(path)
    for files in directory:
        print(files)
        filename = files
        filenameB = bytes(files)
        #size = len(filename)
        #size = bytes(bin(size)[2:].zfill(16),'utf-8') # encode filename size as 16 bit binary
        
        s.send(filenameB)
        print("ProgramMovesHere")
        filename = os.path.join(path,filename)
        #filesize = os.path.getsize(filename)
        #print(filename)
        #print(filesize)
        #filesize = bytes(bin(filesize)[2:].zfill(32),'utf-8') # encode filesize as 32 bit binary
        #s.send(filesize)
        response1 = s.recv(1024)
        if(response1.decode() == "Name_recv"):
            size = os.stat(filename).st_size
            s.send(bytes(str(size)))
            response2 = s.recv(1024)
            #print(response2.decode())
            if(response2.decode() == "Size_recv"):
                file_to_send = open(filename,'rb')
    
                s.sendall(file_to_send.read())
                file_to_send.close()
                print("Finished sendding file")
                #s.send(bytes(' Finished sendding file',encoding = 'utf-8'))
                response3 = s.recv(1024)
                if(response3.decode() == "Good"):
                    os.remove(filename)
                    print('File Sent')
    s.send(bytes("Done"))
    s.close()

if __name__=="__main__":
	File_Send()
