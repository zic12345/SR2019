#!/usr/bin/bash

# Downsample the original NA12878 and YH-1 BAM files to different depth.
# Here we use a python script to conduct batch extraction
# This script needs two parameters, the first one is the total depth you 
# finally want, and the second parameter is "NA" or "YH", which means the
# file you want to downsample.

# e.g. If you want to generate 100X depth mixed files, with YH-1 percent
# 1%, 5%, 10%, 20%, 30% and 40%, first run this script with parameters:
# "100 NA", then run this script with parameters:"100 YH", you will get 
# the downsampled NA12878 and YH-1 BAM files, the depth of NA12878 BAM
# files are: 99X, 95X, 90X, 80X, 70X and 60X, the depth of YH-1 BAM files
# are 1X, 5X, 10X, 20X, 30X and 40X. These downsampled BAM files can be 
# merged using script 5.run_merge.sh to get the 100X depth mixed files
# you wanted

python3 batch_extract.py $1 $2


