import os
import math
import shutil
import glob


batch_size=2000
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
serialNum=0
for i in dividors:
    img_dest="/home/shchang/scratch/cvpr/data/img"+str(serialNum)+"/"
    ann_dest="/home/shchang/scratch/cvpr/data/ann/voc"+str(serialNum)+"/"
    img_source_dir="/home/shchang/scratch/cvpr/data/img/"
    ann_source_dir="/home/shchang/scratch/cvpr/data/ann/voc/"

    for idx,img_filename in enumerate(i):
        img_src_path=img_source_dir+img_filename
        img_dest_path=dest+img_filename
        shutil.copy(img_src_path, img_dest_path)
        os.remove(img_src_path)
        
        ann_filename= a[a.index(img_filename.split(".")[0]+'.xml')]
        a_src_path=ann_source_dir+ann_filename
        a_dest_path=ann_dest+ann_filename
        shutil.copy(a_src_path,a_dest_path)
        os.remove(a_src_path)
        
        
    serialNum=serialNum+1  
