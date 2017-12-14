#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_

import subprocess as sp
# import sys
import re

adapter_list_file = ''


def get_file_names(prefix=False):

    '''
    return a list consists of all file names
    at present working directory
    if give a prefix, return filenames only match it
    '''

    filenames_bytes = sp.check_output('ls')
    filenames_str = filenames_bytes.decode('utf-8').strip()
    if prefix is False:
        result = filenames_str.split('\n')
    else:
        result = []
        for each_filename in get_file_names():
            if each_filename.startswith(prefix):
                result.append(each_filename)
    return result


def pair_FR_readfile(files):
    '''to make read1 file and read2 file pairs'''
    name_pairs = []
    filenames = files[:]
    while len(filenames) > 0:
        target = filenames[0]
        if '_R1_' in target:
            filehead = target[:target.index('_R1_')]
            for i in filenames[1:]:             # searching pair file
                if filehead in i:               # found match
                    name_pairs.append([target, i])
        elif '_R2_' in target:
            filehead = target[:target.index('_R2_')]
            for i in filenames[1:]:             # searching pair file
                if filehead in i:               # found match
                    name_pairs.append([i, target])
        for pairedname in name_pairs[-1]:
            filenames.remove(pairedname)        # remove already paired file
    return name_pairs


def call_trimmomatics(fastq_filename, PE=True):
    '''
    call trimmomatics command from shell
    default with forward and reverse reads
    '''
    exe_path = '/Users/ysh/Trimmomatic-0.36/trimmomatic-0.36.jar'
    base_out = re.match(r'[A-Za-z0-9]+', fastq_filename).group()
    contaminant_file_path = '/Users/ysh/Trimmomatic-0.36/adapters/ig_contaminant.fa'
    sp.check_output('java -jar {} PE -basein {} -baseout {}.trimed.fastq ILLUMINACLIP:{}:2:30:10 SLIDINGWINDOW:4:15 MINLEN:36'.format(exe_path, fastq_filename, base_out, contaminant_file_path), shell=True)

    print('\nTrimming {} done!\n'.format(base_out))


def main():
    pb_files = get_file_names('PB2017')
    tct_files = get_file_names('TCT2017')

    for i in pair_FR_readfile(pb_files):
        call_trimmomatics(i[0])
    for j in pair_FR_readfile(tct_files):
        call_trimmomatics(j[0])


if __name__ == '__main__':
    main()
    print('\n__ done! __\n')
