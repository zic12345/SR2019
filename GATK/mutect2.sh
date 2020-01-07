#!/usr/bin/bash
gatk='/BIGDATA1/scut_hldu_1/work/Low_frequency/NAYH/mix-NA1-YH1/GATK/gatk-4.1.0.0/gatk --java-options -Xmx40g'
ref='/BIGDATA1/scut_hldu_1/work/Low_frequency/NAYH/Genome/UCSC/hg19.fa'
bed='/BIGDATA1/scut_hldu_1/work/Low_frequency/NAYH/Genome/AgilentV5/ex_region.sort.bed'
norm='/BIGDATA1/scut_hldu_1/work/Low_frequency/NAYH/mix-NA1-YH1/100Xnorm/bqsr/bqsr.NA-100X-1.bam'
gnomad='/BIGDATA1/scut_hldu_1/work/Low_frequency/NAYH/mix-NA1-YH1/GATK/bundle/af-only-gnomad.raw.sites.hg19.vcf.gz'
tumor=$1
tumorid=$2
outvcf=$3
(time $gatk Mutect2 \
-R $ref \
-I $tumor \
-I $norm \
-tumor $tumorid \
-normal NAnorm100X \
--germline-resource $gnomad \
--disable-read-filter MateOnSameContigOrNoMappedMateReadFilter \
--native-pair-hmm-threads 24 \
-O $outvcf
)







