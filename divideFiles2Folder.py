import os
import math
import shutil
import glob


batch_size=20000
l=sorted(os.listdir('/home/shchang/scratch/cvpr/data/img/'))
a=sorted(os.listdir('/home/shchang/scratch/cvpr/data/ann/voc/'))
seg=int(math.ceil(len(l)/batch_size))

for i in range(seg):
    foldername='/home/shchang/scratch/cvpr/data/img'+str(i)
    annName='/home/shchang/scratch/cvpr/data/ann/voc'+str(i)
    if os.path.exists(foldername)== False :
        os.mkdir(foldername)
        os.mkdir(annName)
def getDividor(l,batch_size):
    for i in range(1, len(l), batch_size):  
        yield l[i:i + batch_size] 

dividors=getDividor(l,batch_size)
a_dividors=getDividor(a,batch_size)
serialNum=0
for i in dividors:
    dest="/home/shchang/scratch/cvpr/data/img/"+str(serialNum)+"/"
    source="/home/shchang/scratch/cvpr/data/img/"
    dest_a="/home/shchang/scratch/cvpr/data/ann/voc"+str(serialNum)+"/"
    source_a="/home/shchang/scratch/cvpr/data/ann/voc/"
    for idx,filename in enumerate(i):
        print("image file")
        print(filename)
        print("ann file")
        print(a_dividor[idx])
        src_path=source+filename
        dest_path=dest+filename
        a_src_path=source_a+filenamea_dividor[idx]
        a_dest_path=dest_a+filenamea_dividor[idx]
        #print(src_path)
        #print(dest_path)
        #shutil.move(src_path, dest_path)
        shutil.copy(src_path, dest_path)
        os.remove(src_path)
        shutil.copy(a_src_path,a_dest_path)
        os.remove(a_src_path)
        print('------------')
    serialNum=serialNum+1    
