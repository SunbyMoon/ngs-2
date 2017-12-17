#!/usr/bin/python
# _*_ coding: utf-8 _*_

from random import randint


def validate_base_sequence(base_seq, RNAflag=False):
    ''' return True if base sequence is only consist of A, G, C, and T,
    otherwise False'''
    seq = base_seq.upper()
    return len(seq) == (seq.count('A') +
                        seq.count('G') +
                        seq.count('C') +
                        seq.count('U' if RNAflag else 'T'))


def validate_base_sequence_v2(base_seq, RNAflag=False):
    DnaBases = set('ATCGatcg')
    RnaBases = set('AUCGaucg')
    return set(base_seq) <= (set(RnaBases) if RNAflag else set(DnaBases))


def validate_base_sequence_v3(base_seq, RNAflag=False):
    valid_bases = 'UACG' if RNAflag else 'TACG'
    return all([(base in valid_bases) for base in base_seq.upper()])


def gc_content(base_seq):
    assert validate_base_sequence(base_seq), \
            'base sequence has invalid character'
    seq = base_seq.upper()
    return round((seq.count('G') + seq.count('C')) / len(seq), 2)


def random_base(RNAflag=False):
    """return a base randomly, replace T with U if RNAflag is true """
    return ('ACG' + ('U' if RNAflag else 'T'))[randint(0, 3)]


def random_codon(RNAflag):
    """return a codon randomly, replace T with U if RNAflag is true """
    return (random_base(RNAflag) +
            random_base(RNAflag) +
            random_base(RNAflag))


def random_codons(minlength=3, maxlength=10, RNAflag=False):
    return [random_codon(RNAflag) for n in
            range(randint(minlength, maxlength))]


def replace_base_randomly_using_names(base_seq):
    """return a sequence... """
    base_seq = base_seq.upper()
    position = randint(0, len(base_seq) - 1)
    bases = 'ATCG'.replace(base_seq[position], '')

    return (base_seq[:position] +
            bases[randint(0, 2)] +
            base_seq[position+1:])


def read_FASTA_strings(filename):
    with open(filename) as file:
        return file.read().split('>')[1:]


def read_FASTA_entries(filename):
    return [seq.partition('\n') for seq in read_FASTA_strings(filename)]


def read_FASTA_sequences(filename):
    return [[seq[0][1:], seq[2].replace('\n', '')] for seq
            in read_FASTA_entries(filename)]


def read_FASTA_sequences_and_info(filename):
    return [[seq[0].split('|'), seq[1]] for seq in
            read_FASTA_sequences(filename)]


def read_FASTA(filename):
    """Reading fasta sequences with one compact function"""
    with open(filename) as file:
        return [(part[0].split('|'), part[2].replace('\n', '')) for part in
                [entry.partition('\n') for entry in
                 file.read().split('>')[1:]]]


def make_indexed_sequence_dictionary(filename):
    return {info[0]: seq for info, seq in read_FASTA(filename)}


def dr(name):
    """return the result of dir(name), omit any names beginning
    with an underscore """
    return [nm for nm in dir(name) if nm[0] != '_']


def get_FASTA_description(filename):
    with open(filename) as file:
        return [line[1:].split('|') for line in file if line[0] == '>']


def get_FASTA_codes(filename):
    with open(filename) as file:
        if len(line.split('|')) < 3:
            return []
        return {line.split('|')[2] for line in file if line[0] == '>'}


def first_common(list1, list2):
    """Return the first element in list1 that is in list2"""
    return next((item for item in list1 if item in list2), None)


def generate_tripls(chars='TCAG'):
    """return a list of all three-character combinations of
    unique character in chars"""
    chars = set(chars)
    return [b1 + b2 + b3 for b1 in chars for b2 in chars for b3 in chars]


if __name__ == '__main__':
    print(validate_base_sequence('atcccgdd'))
    print(gc_content('atcg'))
    print(random_base())s
