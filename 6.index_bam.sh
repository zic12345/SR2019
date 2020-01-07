#!/bin/bash

# Batch index the merged BAM files

dir=/path/to/merged
yhrun -n 1 -c 24 python3 multiprocess_index_bam.py $dir