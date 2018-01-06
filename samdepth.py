#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_

"""
to mimic samtools depth function
just for practice
usage:

    python3 samdepth.py file.bam file.bed

new:
    for a given bam file, get 4 bases count number at each positions in bed file. 
"""

import pysam
import sys
import pprint

def readbed(filename='~/ngs/data/public_ref_data/ig_tech.bed'):
    """
    read bed file name as input, default is ig_tech.bed file
    return tuple: chromosome number<str>, start position<int>
    note that position number in bed file is 1-based
    """
    with open(filename, 'r') as handle:
        for line in handle:
            line = line.strip()
            try:
                chr_n, start, end = line.split('\t')
                start = int(start)  # in bed file surpose it's 0-based
                end = int(end)
                if start + 1 == end:    # one base is easy
                    yield chr_n, start
                elif start >= end:
                    raise 'bed file format error'
                else:
                    while start < end:  # for multi-base
                        yield chr_n, start
                        start += 1
            except:
                raise "file format error"


def main():
    """
    main job
    """
    samfile = pysam.AlignmentFile(sys.argv[1], 'rb')
    """try:
        for i in readbed('test.bed'):
            contig = i[0]
            start = i[1]    # from .bed file, it is 0-based
            depth = samfile.count(contig, start, start+1)
            print(contig, start+1, depth)   # for human reading, which is 1-based
                                            # pos+1
    finally:
        samfile.close()
    """
    pos_base_cover = {}
    try:
        for each_pos in readbed('test.bed'):
            contig = each_pos[0]
            start = each_pos[1]
            cover = samfile.count_coverage(contig, start, start+1)
            count_A = cover[0][0]
            count_C = cover[1][0]
            count_G = cover[2][0]
            count_T = cover[3][0]
            position_name = contig + '_' + str(start)   # 0-based position
            pos_base_cover[position_name] = {
                                 'A': count_A,
                                 'C': count_C,
                                 'G': count_G,
                                 'T': count_T
                                   }
        pprint.pprint(pos_base_cover)
    finally:
        samfile.close()
        pass


if __name__ == "__main__":
    main()
    print('\ndone\n')
