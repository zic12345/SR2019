#!/bin/bash
manta='/path/to/manta-1.5.0.centos6_x86_64/bin/configManta.py'
reference='/path/to/hg19.fa'
normbam='something'
tumorbam='something'
runpath='something'
bed='/path/to/ex_region.sort.bed.gz'
$manta \
--normalBam $normbam \
--tumorBam $tumorbam \
--referenceFasta $reference \
--runDir $runpath \
--exome \
--callRegions $bed