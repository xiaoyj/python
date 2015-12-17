def cut(path):
	import os
	path_dir = path.rstrip('.jpg')
	if not os.path.exists(path_dir) :
		os.mkdir(path_dir)
	f1=open(path,'r')
	length = len(f1.read())
	print length
	f1.close()
	f1=open(path,'r')
	path_dir = path_dir + '/'
	for i in range(0,length,100000):
		f1r = f1.read(100000)
		f2 = open(path_dir+str(i/100000),'w')
		f2.write(f1r)
		f2.close()
	f1.close()

def together(path):
	import os
	filelist = os.listdir(path)
	f2 = open(path+'/newPhoto.jpg','a')
	filelist = listsort(filelist)
	print filelist
	for num in range(len(filelist)):
		f1 = open(path+'/'+filelist[num],'r')
		f1r = f1.read()
		f2.write(f1r)
		f1.close()
	f2.close()
	
def listsort(list):
	for num in range(len(list)):	
		for j in range(num + 1,len(list),1):	
			if float(list[num]) > float(list[j]):
				temp = list[num]
				list[num] = list[j]
				list[j] = temp
	return list

cut('/home/shaw/DSC7214.jpg')
together('/home/shaw/DSC7214')