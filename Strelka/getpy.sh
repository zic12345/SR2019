#!/bin/bash
strelka2='/path/to/strelka-2.9.7/bin/configureStrelkaSomaticWorkflow.py'
reference='/BIGDATA1/scut_hldu_1/work/Low_frequency/NAYH/Genome/UCSC/hg19.fa'
normbam='something'
tumorbam='something'
runpath='something'
indel='something'
bed='/path/to/ex_region.sort.bed.gz'
$strelka2 \
--normalBam $normbam \
--tumorBam $tumorbam \
--referenceFasta $reference \
--runDir $runpath \
--indelCandidates $indel \
--exome \
--callRegions $bed
