#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_

"""
to statistic kmer in fastq file
input:fastq file path, k(mer length);
out: new file contains information
"""

from Bio import SeqIO
import sys


def main():
    fastq_file = SeqIO.parse(sys.argv[1], 'fastq')
    kmer = int(sys.argv[2])
    kmer_dict = {}
    for entry in fastq_file:
        sequence = str(entry.seq)
        for i in range(len(sequence) - kmer + 1):
            k_seq = sequence[i:i + kmer]
            if k_seq in kmer_dict:
                kmer_dict[k_seq] += 1
            else:
                kmer_dict[k_seq] = 1
    for key, value in kmer_dict.items():
        print('{}:{}'.format(key, value))


if __name__ == '__main__':
    main()
    print('\n done! \n')
