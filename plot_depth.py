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
    depth = dict()  # depth dict structure:
                    # {'chr_NO.' :{
                    #             'pos':[],
                    #             'dep':[]
                    #             }
                    # }
    chr_list = []
    depth_min = 10000
    depth_max = 0

    with open(sys.argv[1]) as handle:
        for line in handle:
            line = line.strip()
            chr, pos, dep = line.split('\t')
            pos = int(pos)
            dep = int(dep)
            if chr not in chr_list:
                chr_list.append(chr)
                depth[chr] = {'pos': [], 'dep': []}
            # if dep > depth_max:
            #     depth_max = dep
            # if dep < depth_min:
            #     depth_min = dep
            depth[chr]['pos'].append(pos)
            depth[chr]['dep'].append(dep)

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
