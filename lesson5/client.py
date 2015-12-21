import socket
import os
import sys
import json

class MyClient:
    def __init__(self,host,port,defaultPath):
        self.host = host
        self.port = port
        self.defaultPath = defaultPath
    def pullRequest(self):
        sock = socket.socket()
        sock.connect((self.host,self.port))
        filePostion = ''
        f = None
        while True:
            print 'please input the order'
            order = sys.stdin.readline()
            sock.sendall(order)
            result = sock.recv(1024)
            try:
                receiveData = json.loads(result)
                try:
                    if receiveData.startswith('list'):
                        filesNumber = int(receiveData[4:])
                        if filesNumber == 1:
                            receiveNumber = sock.recv(128)
                            passNumber = int(receiveNumber)
                            i = 0
                            while i < passNumber:
                                sock.sendall(str(i))
                                receiveFile = sock.recv(100000)
                                f.write(receiveFile)
                                i = i + 1
                            f.close()
                            print 'download succeed'
                        else:
                            for filesNumbers in range(0,filesNumber,1):
                                receiveNumber = sock.recv(128)
                                passNumber = int(receiveNumber)
                                i = 0
                                while i < passNumber:
                                    sock.sendall(str(i))
                                    receiveFile = sock.recv(100000)
                                    f.write(receiveFile)
                                    i = i + 1
                                f.close()
                                print 'download succeed'
                except:
                    print receiveData
            except:
                print result
                if result.startswith('are you'):          #create the file
                    result = result.split(':')[1].split('\n')[0].strip()
                    if not os.path.exists(self.defaultPath) :
                        os.mkdir(self.defaultPath)
                    filePostion = self.defaultPath +'/' + result
                    f = open(filePostion,'w')
                elif result == 'download canceled\n':    # delete the file
                    os.remove(filePostion)
                    filePostion = ''

if __name__ == '__main__':
	print 'Client is in processing'
	cli = MyClient('127.0.0.1',5001,'/home/shaw/downloadByShaw')
	cli.pullRequest()
