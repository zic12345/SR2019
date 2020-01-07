#!/usr/bin/env python3
#batch run BQSR2.sh for files in a certain path
import os,sys
from multiprocessing import Pool
wkdir=sys.argv[1]

def bqsr(script):
    os.system(script)

if __name__ == '__main__':
    files = sorted([x for x in os.listdir(wkdir) if ((x.endswith(".cram"))|(x.endswith(".bam")))])
    p=Pool(6)

    for file in files:
        report=file+'.report'
        bqsrbam='bqsr.'+file
        script='/absolute/path/to/BQSR2.sh %s %s %s %s'%(wkdir,file,report,bqsrbam)
        p.apply_async(bqsr,args=(script,))
    p.close()
    p.join()
