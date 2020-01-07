#!/usr/bin/bash

# Raw data QC using fastp
# specify paths for softwares and input/output files
fastp='/path/to/fastp'

# infile
NA12878_1='/path/to/NA12878.r1.fq.gz'
NA12878_2='/path/to/NA12878.r2.fq.gz'
YH_1='/path/to/YH.r1.fq.gz'
YH_2='/path/to/YH.r2.fq.gz'

# outfile
NAout1='/path/to/naout.r1.fq.gz'
NAout2='/path/to/naout.r2.fq.gz'
NA12878js='/path/to/na12878.json'
NA12878html='/path/to/na12878.html'
YHout1='/path/to/yhout.r1.fq.gz'
YHout2='/path/to/yhout.r2.fq.gz'
YHjs='/path/to/yh.json'
YHhtml='/path/to/yh.html'
logNA='/path/to/na.log'
logYH='/path/to/yh.log'

# run fastp
(time yhrun -N 1 -n 1 $fastp -w 24 -j $NA1287js -h $NA12878html -R "NA fastp Report" -i $NA12878_1 -o $NAout1 -I $NA12878_2 -O $NAout2) 2>&1 > $logNA
(time yhrun -N 1 -n 1 $fastp -w 24 -j $YHjs -h $YHhtml -R "YH fastp Report" -i $YH_1 -o $YHout1 -I $YH_2 -O $YHout2) 2>&1 > $logYH
# note:"yhrun" is the command which submit jobs to the computer clusters, we allocated 1 node and 24 threads for fastp.