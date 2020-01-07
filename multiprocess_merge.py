#!/usr/bin/env python3
import os,sys
from multiprocessing import Pool
os.chdir(sys.argv[1])
na = [x for x in os.listdir() if 'NA' in x]
total_depth = int(sys.argv[2])

def merge_bam(out,bam1,bam2):
    script = "samtools merge -n -@ 3 %s %s %s"%(out,bam1,bam2)
    os.system(script)


if __name__ == "__main__":
    p = Pool(8)
    result = []
    for naname in na:
        num = naname.split(".")[0].split("-")[-1]
        na_depth = int(naname.split(".")[0].split("-")[1].split('X')[0])
        yh_depth = total_depth - na_depth
        yhname = "YH-%sX-%s.bam"%(yh_depth,num)
        bam1 = os.path.abspath(naname)
        bam2 = os.path.abspath(yhname)
        out = os.path.join(os.path.split(os.getcwd())[0],"NAYH-%sX-%sX-somatic-%s.bam"%(na_depth,yh_depth,num))
        result.append(p.apply_async(merge_bam,args=(out,bam1,bam2)))
    p.close()
    p.join()
