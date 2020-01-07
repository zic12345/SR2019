#!/usr/bin/env python3

# batch start Strelka2 somatic mode on computer cluster, require 4 parameters: normal BAM file dir, 
# tumor BAM file dir, work dir and the according manta result directory (the 3rd parameter of 1.batch_manta.py)  

import os,sys,shutil
import subprocess as sub
normdir = sys.argv[1]
tumordir = sys.argv[2]
workdir = sys.argv[3]
depthN = sys.argv[4]
tumordic={x:os.path.join(tumordir,x) for x in os.listdir(tumordir) if ((x.endswith(".bam"))|(x.endswith(".cram")))}
normdic={x[-5]:os.path.join(normdir,x) for x in os.listdir(normdir) if ((x.endswith(".bam"))|(x.endswith(".cram")))}

if not os.path.exists(workdir):
    os.makedirs(workdir,exist_ok=True)
os.chdir(workdir)
manta_dir = os.path.join(os.path.split(workdir)[0],"manta-%sNorm"%depthN)
strelkash = "Strelka.sh"

with open('getpy.sh') as f:
    getpy = f.readlines()

for file in tumordic:
    tumor_abspath = tumordic[file]
    tmp = getpy.copy()

    os.makedirs(file.split(".")[0],exist_ok=True)
    os.chdir(file.split(".")[0])
    shutil.copy(strelkash,"./")
    norm_abspath = normdic['1']
    manta_path = os.path.join(manta_dir,file.split(".")[0],"results/variants/candidateSmallIndels.vcf.gz")
    tmp[4] = tmp[4].replace("something",norm_abspath)
    tmp[5] = tmp[5].replace("something",tumor_abspath)
    tmp[6] = tmp[6].replace("something",os.getcwd())
    tmp[7] = tmp[7].replace("something",manta_path)
    with open("getpy.sh",'w') as f:
        f.writelines(tmp)
    os.system("chmod +x ./getpy.sh")
    process = sub.Popen("./getpy.sh",shell=True)
    ret = process.wait()
    if ret == 0:
       os.system("yhbatch Strelka.sh")
    os.chdir("..")