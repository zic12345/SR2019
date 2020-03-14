# SR2019
All codes used to generate data in article "Systematic comparison of somatic variant calling performance among different sequencing depth and mutation frequency"

If you have problems, please contact the authors or submit issues.

## bam files
The 90 mixed bam files will be available in about a week via BaiduNetDisk.

## Noticing
When you downsampled and mixed the bam files, all of the RG tags in NA.md.bam and YH.md.bam will be kept, Strelka2 ignores RG tags so the result won't be affected, however, the result of programs which needs the information of RG tags such as GATK mutect2 will be afffected, **thus you need to run RG tag replacement on the mixed bam files before calling mutations**.
