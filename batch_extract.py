#!/usr/bin/env python3
import os,sys
from multiprocessing import Pool

# the original depth of NA12878 and YH-1
nadepth=812.40
yhdepth=407.25
work_dph=int(sys.argv[1])

napercent = [0.99,0.95,0.90,0.80,0.70,0.60]
yhpercent = [0.01,0.05,0.10,0.20,0.30,0.40]

yhpercent = [0.05]
NAtotal='/path/to/na.addRG.mdup.bam'
YHtotal='/path/to/yh.addRG.mdup.bam'
downsample="java -Xmx3000m -Djava.io.tmpdir=/BIGDATA1/scut_hldu_1/tmp -jar /BIGDATA1/scut_hldu_1/bin/picard.jar DownsampleSam"

# Important! Random seed must NOT be changed! Or you won't get the same bam file!
seeds = {1:6666,2:8888,3:9999}

def extract(script):
    os.system(script)


p=Pool(18)
if sys.argv[2]=='NA':
    for i in napercent:
        na_dph = int(work_dph*i)
        p_na = na_dph/nadepth
        for a in seeds:
            rand_seed = seeds[a]
            script = "%s I=%s O=NA-%sX-%s.bam R=%s P=%s A=0.00000001"%(downsample,NAtotal,na_dph,a,rand_seed,p_na)
            p.apply_async(extract,args=(script,))

elif sys.argv[2]=='YH':
    for i in yhpercent:
        yh_dph = int(work_dph*i)
        p_yh = yh_dph/yhdepth
        for a in seeds:
            rand_seed = seeds[a]
            script = "%s I=%s O=YH-%sX-%s.bam R=%s P=%s A=0.00000001"%(downsample,YHtotal,yh_dph,a,rand_seed,p_yh)
            p.apply_async(extract,args=(script,))

p.close()
p.join()
