#!/usr/bin/bash

# remove duplications using picard
naI='/path/to/na.addRG.bam'
naO='/path/to/na.addRG.mdup.bam'
naD='/path/to/na.dup.txt'
yhI='/path/to/yh.addRG.bam'
yhO='/path/to/yh.addRG.mdup.bam'
yhD='/path/to/yh.dup.txt'
NAlog='/path/to/na.dup.log'
YHlog='/path/to/yh.dup.log'

(time yhrun -N 1 -n 1 java -jar $picard MarkDuplicates  \
 I=$naI  \
 O=$naO \
 M=$naD \
 REMOVE_DUPLICATES=true \
 ASO=coordinate \
 CREATE_INDEX=true) 2>&1 >$NAlog

(time yhrun -N 1 -n 1 java -jar $picard MarkDuplicates  \
 I=$yhI  \
 O=$yhO \
 M=$yhD \
 REMOVE_DUPLICATES=true \
 ASO=coordinate \
 CREATE_INDEX=true) 2>&1 >$YHlog
