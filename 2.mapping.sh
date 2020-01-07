#!/usr/bin/bash

# mapping to hg19 reference genome using bwa mem
# specify paths for softwares and input/output files
hg19='/path/to/hg19'
bwa='/path/to/bwa'
picard='/path/to/picard.jar'
NA12878_1='/path/to/naout.r1.fq.gz'
NA12878_2='/path/to/naout.r2.fq.gz'
YH_1='/path/to/yhout.r1.fq.gz'
YH_2='/path/to/yhout.r2.fq.gz'
NAsam='/path/to/nasam.sam'
NAbam='/path/to/na.addRG.bam'
YHsam='/path/to/yhsam.sam'
YHbam='/path/to/yh.addRG.bam'
logNAmap='/path/to/na.log'
logYHmap='/path/to/yh.log'
lognatrans='/path/to/lognatrans.log'
logyhtrans='/path/to/logyhtrans.log'

# run bwa mem
(time yhrun -N 1 -n 1 $bwa mem -t 6 $hg19 $NA12878_1 $NA12878_2 > $NAsam ) 2>&1 > $logNAmap

(time yhrun -N 1 -n 1 $bwa mem -t 6 $hg19 $YH_1 $YH_2 > $YHsam ) 2>&1 > $logYHmap

# convert SAM to BAM and add read groups
(time yhrun -N 1 -n 1 java -jar $picard AddOrReplaceReadGroups  \
I=$NAsam  \
O=$NAbam \
RGID=NA \
RGLB=WES \
RGPL=Illumina \
RGPU=Novaseq \
RGSM=NA \
SO=coordinate \
CREATE_INDEX=true ) 2>&1 > $lognatrans

(time yhrun -N 1 -n 1 java -jar $picard AddOrReplaceReadGroups  \
I=$YHsam  \
O=$YHbam \
RGID=YH \
RGLB=WES \
RGPL=Illumina \
RGPU=Novaseq \
RGSM=YH \
SO=coordinate \
CREATE_INDEX=true ) 2>&1 > $logyhtrans