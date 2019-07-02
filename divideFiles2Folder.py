import os
import math
import shutil
import glob


batch_size=20000
l=os.listdir('/home/shchang/scratch/cvpr/data/img/')
seg=int(math.ceil(len(l)/batch_size))

for i in range(seg):
    foldername='/home/shchang/scratch/cvpr/data/img/'+'img'+str(i)
    if os.path.exists(foldername)== False :
        os.mkdir(foldername)
   
def getDividor(l,batch_size):
    for i in range(1, len(l), batch_size):  
        yield l[i:i + batch_size] 

dividors=getDividor(l,batch_size)
serialNum=0
for i in dividors:
    dest="/home/shchang/scratch/cvpr/data/img/img"+str(serialNum)+"/"
    source="/home/shchang/scratch/cvpr/data/img/"
    for idx,filename in enumerate(i):
        print(filename)
        src_path=source+filename
        dest_path=dest+filename
        print(src_path)
        print(dest_path)
        #shutil.move(src_path, dest_path)
        shutil.copy(src_path, dest_path)
        os.remove(src_path)
        print('------------')
    serialNum=serialNum+1
