import os 
import glob
import time
import shutil
from itertools import chain
from functools import reduce
import re
import subprocess

count=0
suffix=[]
with open("iter.txt","r") as f:
	for line in f:
	    suffix.append(int(line))
	    count=count +1

def findJobID(slurmIdsArr):
    temp=list(map(lambda path:path.split("slurm-"),slurmIdsArr))
    temp2=list(map(lambda comb:int(comb[1].replace(".out","")),temp)) 
    temp2.sort()
    return(temp2[len(temp2)-1])
	
	
while count>0:
	slurmIdsArr= glob.glob("slurm*")
	job_id=findJobID(slurmIdsArr)
	slurm_path="slurm-"+str(job_id)+".out"
	print(count)
	train_file="./temp/"+"temp_list"+"."+str(suffix[count-1])
	test_file="./temp/"+"temp2_list"+"."+str(suffix[count-1])
	
	result = subprocess.run(['squeue', '-j',str(job_id)], stdout=subprocess.PIPE)
	time.sleep(120)
	while(result.stdout.decode('utf-8') is not ''):
	    time.sleep(450)
	    result = subprocess.run(['squeue', '-j',str(job_id)], stdout=subprocess.PIPE)

	os.remove("./temp_list")
	os.remove("./temp2_list")
	shutil.move(train_file,"./temp_list")
	shutil.move(test_file,"./temp2_list")
	subprocess.call("../residual-attention-network/run/autorun.sh",shell=True)
	time.sleep(450)        
		

	count=count-1
	print(count)
