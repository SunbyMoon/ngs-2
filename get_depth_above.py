#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_
"""
this is a python stript to isolate loci with depth more than a given number
  input1: depth file exported from samtools depth
          (tab seperated 3 columns: reference name, position, depth)
  input2: a depth thrshold
  output: a new depth file with depth above given threshold
"""

import sys


def main():
    depth_threshold = int(sys.argv[2])
    raw_filename = sys.argv[1]
    out_filename = raw_filename + '.depth' + str(depth_threshold)
    print('scaning file "{}" with depth no less than {}'.format(raw_filename, depth_threshold))
    raw_count = 0
    new_count = 0
    with open(out_filename, 'w') as writehandle:
        with open(sys.argv[1]) as readhandle:
            for line in readhandle:
                line = line.strip()
                raw_count += 1
                depth = int(line.split('\t')[-1])
                if depth >= depth_threshold:
                    writehandle.write(line + '\n')
                    new_count += 1
    trim_percent = round(100 * new_count / raw_count, 2)
    print('{}/{} position isolated : {}%'.format(new_count, raw_count, trim_percent))


if __name__ == '__main__':
    main()
    print('done!')
