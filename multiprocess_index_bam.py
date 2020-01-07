#!/usr/bin/env python3
import os,sys
from multiprocessing import Pool
os.chdir(sys.argv[1])
files = [x for x in os.listdir() if (x.endswith(".cram"))|(x.endswith('.bam'))]

def replaceRG(infile):
    script = "samtools index -@ 2 %s"%infile
    os.system(script)

if __name__ == "__main__":
    p=Pool(12)
    for infile in files:
        p.apply_async(replaceRG,args=(infile,))
    p.close()
    p.join()
