#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import gzip     # for gzip compressed file
import bz2      # for bzip2 compressed file
from Bio import SeqIO


def main():
    filename = sys.argv[1]
    if filename.endswith('.zip'):
        with gzip.open(filename, "rt") as handle:
            seqfile = SeqIO.parse(handle, 'gb')
            print next(seqfile).id


main()
