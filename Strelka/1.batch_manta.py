#!/usr/bin/env python3

# batch start manta software on computer cluster, require 3 parameters: normal BAM file dir, 
# tumor BAM file dir and work dir 

import os,sys,shutil
import subprocess as sub
normdir = sys.argv[1]
tumordir = sys.argv[2]
workdir = sys.argv[3]

tumordic={x:os.path.join(tumordir,x) for x in os.listdir(tumordir) if ((x.endswith(".bam"))|(x.endswith(".cram")))}
normdic={x[-5]:os.path.join(normdir,x) for x in os.listdir(normdir) if ((x.endswith(".bam"))|(x.endswith(".cram")))}

if not os.path.exists(workdir):
    os.makedirs(workdir,exist_ok=True)
os.chdir(workdir)

mantash = "manta.sh"

with open('getmanta.sh') as f:
    getpy = f.readlines()

for file in tumordic:
    tumor_abspath = tumordic[file]
    tmp = getpy.copy()
    os.makedirs(file.split(".")[0],exist_ok=True)
    os.chdir(file.split(".")[0])
    shutil.copy(mantash,"./")
    norm_abspath = normdic['1']
    tmp[4] = tmp[4].replace("something",norm_abspath)
    tmp[5] = tmp[5].replace("something",tumor_abspath)
    tmp[6] = tmp[6].replace("something",os.getcwd())
    with open("getmanta.sh",'w') as f:
        f.writelines(tmp)
    os.system("chmod +x ./getmanta.sh")
    process = sub.Popen("./getmanta.sh",shell=True)
    ret = process.wait()
    if ret == 0:
       os.system("yhbatch manta.sh")
    os.chdir("..")
