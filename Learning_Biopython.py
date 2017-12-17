#!/usr/bin/python
#!_*_ coding:utf-8 _*_

import subprocess
import sys
from Bio import SeqIO
from Bio import AlignIO
from Bio import pairwise2
from Bio.Alphabet import generic_dna
from Bio.Alphabet import generic_nucleotide
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import glob
from Bio.Align.Applications import ClustalwCommandline
from Bio.Align.Applications import MuscleCommandline
from Bio import Phylo
from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Blast.Applications import NcbiblastxCommandline
from Bio import motifs


seq_1 = SeqIO.parse('../data/ls_orchid.fasta', 'fasta')
seq_2 = SeqIO.read('../data/NC_005816.fna', 'fasta')
seq_3 = SeqIO.read('../data/NC_005816.gb', 'genbank')
seq_5 = SeqIO.parse('../data/ls_orchid.gbk', 'genbank')


result_handle = NCBIWWW.qblast('blastn', 'nt', '''ATGTACGTAAATGGAAAAATTTCTGGATTTCGGCAACAAAACTTCCTATATCCGCTACTCTTTCAGGAGT
ATATTTACTCACTTGCTCATGATCATAACTTCAATAGTTTGATTTTTTACGAACCCGTGGAAATTATTGG
TTATGACAATAAATCTAGTTTAGTACTTGTGAAACGTTTAATTACTCAAATGTATCAACAGAATTTTTTT
ATTTCTTCGTTTAATGATTCTAACAAAAAAGAATTTTGGGAGTACAAGAATTTTTTTTCTTCTCATTTTT
CTTCTCAAATGGTATCAGAAGGTTTTGGAGTCATTCTGGAAATTCCATTCTCGTCGCAATTAGTATCTTT
TTCTGAATCTTCTGAAGCAAAAAAAATACTAAAATATCAGAATTTACGATCTATTCATTCAATATTTCCC
TTTTTAGAGGACAAATTTTTACATTTGAATTATGTGTCAGATCTACTAATACCTCATCCCATACATCTGG
AAATCTTGGTTCAAGTACTTCAATGCTGGATCAAGGATGTTCCTTCTTTGCATTTATTGCGATTTCTTTT
CCACGAATATCATAATTTGAATAGTCTCGTTACTTCAAAGAAATTCATTTACGCCTTTTCAAAAATAAAG
AAAAAATTCCTTTGGTTCCTATATAATTCTTATGTATATGAATGCGAATATTTATTCCTATTTATTCGTA
AACAATCTTCTTATTTACGATCAACATCCTCTGGAGTCTTTCTTGAGCGAACACATTTCTATGTAAAAAT
AGAGCATCTTATAGTAGTGTGTTGTAATTCTTTTCAGAAGATCCTATGCTTTCTCAAGGATACTTTCATG
CATTATGTTCGATATCAAGGAAAGGCAATTCTGGCTTCAAAGGGAACTCTTATTCTGATGAATAAATGGA
AATTTCATCTTGTGAATTTTTGGCAATCTTATTTTCACTTTTGGTCTCAACCGTATAGGATCCATATAAA
GCAATTATCCAACTATTCCTTCTCTTTTCTGGGGTATTTTTCAAGTGTACTAGAAAATCATTTGGTAGTA
AGAAATAAAATGCTAGAGAATTCATTTCTAATAAATATTATGACTCATAGATTATATACCATAGTCCCAG
TCATGTCTCTTATTGGATCATTGTCGAAAGCTCAATTTTGTACTGTATTGGGTCATCCTATTAGTAAACC
GATCTGGACCGATTTATCGGATTCTGATATTATTGATCGATTTTGCCGGATATGTAGAAATCTTTGTCGT
TATCACAGTGGATCCTCAAAAAAACAGGTTTTGTATCGTATAAAGTATATACTTCGACTTTCATGTGCTA
GAACTTTGGCGCGGAAACATAAAAGTACAGTACGCACTTTTATGCGAAGATTAGGTTCGGGATTATTAGA
AGAATTCTTTATGGAAGAAGAACAAGTTCTTTCTTTAATCTTCCTCCAAAAAATCCCTTTTCCCTTGTAC
GGATCACATATAGACCGTATTTGGTATTTGGACATTATGCATATCAATGATCTGGTGGATAATTCATGA''')
blast_record = NCBIXML.read(result_handle)
print blast_record.alignments

'''

with open('my_blast.xml','w') as out_handle:
    out_handle.write(result_handle.read())

result_handle.close()

result_handle = open('my_blast.xml')
'''
'''

seq_write_file = SeqIO.write(my_record,'my_example.faa','fasta')
SeqIO.convert('ls_ochid.gbk','genbank','my_example.fasta','fasta')

records = [rec.reverse_complement(id = 'rc'+rec.id,description = 'reverse complement') \
           for rec in SeqIO.parse('ls_orchid.fasta','fasta') ]

#three ways to make sequence records into dictionary
#1：
orchid_dict = SeqIO.to_dict(SeqIO.parse('../data/ls_orchid.gbk','genbank'))

#2：
#seq_4 = SeqIO.index('../data/GRCh38_latest_genomic.fna','fasta')

#3：
file_1 = glob.glob('../data/gbvrl*.seq')
gb_vrl = SeqIO.index_db('gbvrl.idx',file_1,'genbank')
'''
'''

clustalw2_exe = r'../clustalw-2.1-macosx/clustalw2'
cline_1 = ClustalwCommandline(clustalw2_exe, infile = '../data/opuntia.fasta')
align_1 =  AlignIO.read('../data/opuntia.aln','clustal')
tree_1 = Phylo.read('../data/opuntia.dnd','newick')

print align_1
Phylo.draw_ascii(tree_1)
'''
'''
cline_2 = MuscleCommandline(r'../muscle3.8.31/src/muscle',input= '../data/opuntia.fasta',out='../data/opuntia.txt',clw = True)
align_2 = AlignIO.read('../data/opuntia.txt','clustal')
print align_2
'''


'''
print '%i sequences indexed'%len(gb_vrl)
print '%i files to index'%len(file_1)
'''
'''
orchid_dict = SeqIO.to_dict(SeqIO.parse('../data/ls_orchid.gbk','genbank'))
print orchid_dict.keys()

#print seq_1.next()
'''
'''
print seq_5.next().annotations['organism']
latin_list =  [seq_record.annotations['organism'] for seq_record in seq_5]
latin_set = set(latin_list)

for item in latin_set:
    print item
print len(latin_set)
'''
'''
i = 1
for record in seq_4:
    print i,'\t',record.name,'\t',len(record.seq)
    i += 1

'''
'''
len_list = []
for each_record in seq_record:
    len_list.append(len(each_record.seq))

print max(len_list),min(len_list),

i = 1
while i >0 :
    print seq_record_1.next().name,'\n'
    print seq_record_2
    i -= 1
'''