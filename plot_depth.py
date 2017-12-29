#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_

"""
this is a python script to draw a depth file outputed from <samtools depth>
command. for instance, execute:

    $ samtools depth sample1.bam > sample1.depth

in 'sample1.depth' file: each line consists of:
    chromosomr_ID   position_NO. coverage_Count
three column seperated with tab separator '\t'

to draw this information, execute:

    $ python3 plot_depth.py sample1.depth

a Python launcher will be loaded, you can see now.
"""

import matplotlib.pyplot as plt
import sys


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
    main()
