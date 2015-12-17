def cut(path):
	f=open(path,'r')
	print f.read()
	length = len(f.read())
	f.close();
	f=open(path,'r')
	for i in range(length):
		print f.read(1024)
		i = i+1024

cut('/home/shaw/hello.txt')