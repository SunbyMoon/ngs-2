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


def read_bed(filename_bed):
    """parse .bed file
    """
    with open(filename_bed) as handle:
        for line in handle:
            line = line.strip()
            try:
                [chromo, start, end] = line.split('\t')[:3]
                start = int(start)
                end = int(end)
                yield chromo, start, end
            except:
                print('not good bed file format')


def main():
    """main job, read bam file and write new bam file
    """
    filename_bed = sys.argv[1]
    filename_bam = sys.argv[2]

    infile = pysam.AlignmentFile(filename_bam, 'rb')
    outfile = pysam.AlignmentFile(filename_bam + '.bed_strict.bam', 'w')
    for each_pos in read_bed(filename_bed):
        fetch_reads = infile.fetch(each_pos[0], each_pos[1], each_pos[2])
        for each_read in fetch_reads:
            outfile.write(each_read)


if __name__ == '__main__':
    main()
    print('\n--end--\n')
