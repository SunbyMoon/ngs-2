#!/usr/bin/python
# _*_ coding: utf-8 _*_

from Bio import SeqIO
from Bio.SeqUtils.CheckSum import sequid

# in memory way:
def accession(record):
    """
    given a SeqRecord, return the accession number as a string.
    e.g. "gi|2765613|emb|Z78488.1|PTZ78488" -> "Z78488.1"
    """
    parts = record.id.split('|')
    assert len(parts) == 5 and parts[0] == 'gi' and parts[2] == 'emb'
    return parts[3]


seq_dict = SeqIO.to_dict(SeqIO.parse('filename or handle', 'fasta'), key_function=get_accession)

seq_dict = SeqIO.to_dict(SeqIO.parse('filename or handle', 'fasta'), lambda rec : sequid(rec.seq))

# by indexed files way
seq_dict = SeqIO.index('filename or handle', 'fasta', key_function=)
seq_dict.close()

# by database
import glob
files = glob.glob("gbvrl*.seq")
gb_vrl = SeqIO.index_db('gbvrl.idx', files, 'genbank')
