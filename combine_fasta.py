#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys


def combine_fasta_seqs(seq_file_string):
    seqs = ""
    fastas_list = seq_file_string.split('>')[1:]
    for each_fasta in fastas_list:
        seq = ''.join(each_fasta.split('\n')[1:])
        seqs += seq

    return seqs


def main():
    filename = sys.argv[1]
    with open(filename) as file:
        fasta_string = file.read()
    combined_seq = combine_fasta_seqs(fasta_string)
    combined_query = '>new combined sequence record\n' + combined_seq
    with open(sys.argv[1] + '_combined.txt', 'w') as write_file:
        write_file.write(combined_query)


if __name__ == "__main__":
    main()
