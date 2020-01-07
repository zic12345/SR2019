#!/usr/bin/env python3
#batch run mutect2.sh for files in a certain path
import os,sys
os.chdir(sys.argv[1])
files = [x for x in os.listdir() if ((x.endswith(".bam"))|(x.endswith(".cram")))]
os.mkdir("mutect")

for file in files:
    outgzvcf = "mutect/"+file+".vcf.gz"
    NAdepth=file.split("-")[1][:-1]
    YHdepth=file.split("-")[2][:-1]
    totaldepth = int(NAdepth)+int(YHdepth)
    YHpercent = int(YHdepth)/int(totaldepth)
    num = file.split("-")[4].split('.')[0]
    rgid="mix%sX_YH%s_%s"%(totaldepth,YHpercent,num)
    script = "yhbatch /path/to/mutect2.sh %s %s %s"%(file,rgid,outgzvcf)
    os.system(script)

# "yhbach" is the command which submit batch jobs to the computer clusters, we allocated 1 node and 24 threads for fastp.