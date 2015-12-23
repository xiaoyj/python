import socket
import os
import json

class MyServer:
	def  __init__(self,host,port):
		self.host = host
		self.port = port
	def connect(self):
		s = socket.socket()
		s.bind((self.host,self.port))
		s.listen(5)
		isDownloading = False
		fileToSendDict ={}
		connection,adress = s.accept()
		while True:
			receiveData = connection.recv(1024)
			filelist = self.getFilesList('/home/shaw/share')
			if not receiveData:
				continue
			elif receiveData == 'hi,server!\n':
				connection.sendall('hi,client!')
			elif receiveData == 'ls\n':
				json_filelist = json.dumps(filelist)
				connection.sendall(json_filelist)
			elif receiveData.startswith('download'):
				try:
					index = int(receiveData[9])
					fileToSendDictList = []
					if os.path.isdir(filelist[index]):
						for root,dirs,files in os.walk(filelist[index]):
							for fn in files:
								fileToSendDict = self.readFiles(fn)
								fileToSendDictList.append(fileToSendDict)
						connection.sendall('are you sure to download files included in: ' + filelist[index].split("/")[-1]+'\nreply with yes or no')
					else:
						fileToSendDict = self.readFiles(filelist[index])
						fileToSendDictList.append(fileToSendDict)
						connection.sendall('are you sure to download file: ' + filelist[index].split("/")[-1]+'\nreply with yes or no')
					isDownloading = True
				except:
					connection.sendall('file not exist')
			elif receiveData == 'yes\n'and isDownloading:
				connection.sendall('list' + str(len(fileToSendDictList)))
				for filesDict in fileToSendDictList:
					connection.sendall(str(len(filesDict)))
					i = 0
					while True:
						receiveNumber = connection.recv(1024)
						i = int(receiveNumber)
						connection.sendall(filesDict[i])
						if i == len(filesDict) - 1:
							break
				isDownloading = False
				fileToSendList ={}
			elif receiveData == 'no\n'and isDownloading:
				connection.sendall('download canceled')
				isDownloading = False
				fileToSendList ={}
			else:
				connection.sendall('wrong order')
		sock.close()
	def getFilesList(self,findPath):
		fileList = []
		fileNames = os.listdir(findPath)
		if(len(fileNames) > 0):
			for fn in fileNames:
				fullFileNames = os.path.join(findPath,fn)
				fileList.append(fullFileNames)
		return fileList

	def readFiles(self,path):
		fileTxt = {}
		f = open(path,'r')
		length = len(f.re               ad())
		f.close()
		f = open(path,'r')
		for i in range(0,length,100000):
			fileTxt[int(i/100000)] = f.read(100000)
		f.close()
		return fileTxt


if __name__ == '__main__':
	print 'Server is in processing'
	ser = MyServer('127.0.0.1',5001)
	ser.connect()
