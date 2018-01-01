#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_

"""
This is a python script to retrive all reads mapped to regions in .bed file.
Input: .bed <region_file>
       .bam <raw_mapping_file>
Output: .bam <extracted_mapping_file>

>USAGE: python3 get_bed_reads.py regions1.bed sample_a.bam
"""

import pysam
import sys


def read_bed():
    """parse .bed file
    """
    pass


def read_bam():
    """read .bam file with pysam module
    """
    pass


def main():
    """main job
    """
    pass


if __name__ == '__main__':
    main()
    print('\n--end--\n')
