#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_

import matplotlib.pyplot as plt
import sys


def usage():
    message = """
this is a python script to draw a depth file outputed from <samtools depth>
command. for instance, if you execute:

    $ samtools depth sample1.bam > sample1.depth

in 'sample1.depth' file: each line consists of:

<chromosomr_ID>\t<position_NO.>\t<coverage_Count>

to draw this information, execute:

    $ python3 plot_depth.py sample1.depth

a Python launcher will be loaded, you can see now.
"""
    print(message)


def main():
    depth = dict()
    chr_list = []
    with open(sys.argv[1]) as handle:
        for line in handle:
            line = line.strip()
            chr, pos, dep = line.split('\t')
            if chr not in chr_list:
                chr_list.append(chr)
                depth[chr] = {'pos': [], 'dep': []}
            depth[chr]['dep'].append(int(dep))
            depth[chr]['pos'].append(int(pos))

    for i in range(0, len(chr_list)):
        plt.subplot(len(chr_list), 1, i + 1)
        plt.plot(depth[chr_list[i]]['pos'], depth[chr_list[i]]['dep'])
        plt.ylabel(chr_list[i])
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) == 2 and '.depth' in sys.argv[1]:
        main()
    else:
        usage()
