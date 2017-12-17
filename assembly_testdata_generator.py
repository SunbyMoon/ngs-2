#!/usr/bin/python
# _*_ coding: utf-8 _*_

import random_dna
import itertools
# import StringIO


def fastamaker(seqlist):
    outstring = ''
    id = itertools.count(1, 1)
    for seq in sorted(seqlist):
        outstring += '>seq{}\n{}\n'.format(next(id), seq)
    return outstring


def cut(sequence):
    """
    cut sequence into a list of subsequence, with overlap
    """
    length = 10
    result = []
    start = 0
    while start < len(sequence) - length:
        result.append(sequence[start:start + length])
        start += 5
    return result


def main():
    raw_sequence = random_dna.randomdnaseq(30)
    cutseq = cut(raw_sequence)
    fasta_str = fastamaker(cutseq)
    print raw_sequence
    print fasta_str

    with open('cut_data.fasta', 'w') as handle:
        handle.write(fasta_str)


if __name__ == '__main__':
    main()
