#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import random
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


def randm_sub_reads(superSeq, length, count):
    superSeq = superSeq.upper()
    result_pool = []
    startLimit = len(superSeq) - length
    i = 0
    while i < count:
        startPos = random.randint(0, startLimit)
        substring = superSeq[startPos:startPos + length]
        result_pool.append(substring)
        i += 1
    return result_pool


def main():
    filename = sys.argv[1]
    [l, n] = map(int, sys.argv[2:4])
    fasta = SeqIO.parse(filename, 'fasta')
    sub_reads = []
    i = 0
    for entry in fasta:
        seq = str(entry.seq)
        for each in randm_sub_reads(seq, l, n):
            read = SeqRecord(Seq(each),
                             id=entry.id + '_sub' + str(i),
                             description='sub reads',
                             letter_annotations={'phred_quality': [65]*int(l)})
            i += 1
            sub_reads.append(read)
    SeqIO.write(sub_reads, filename.split('.')[0] + '_sub.fastq', 'fastq')


if __name__ == '__main__':
    main()
