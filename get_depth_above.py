#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_

import sys


def usage():
    message = """this is a python stript to isolate loci with depth more than a given number
  USAGE: python3 get_depth_above.py <depth_file> <threshold>
  <depth_file>: Plain-Text File, Output of "samtools depth" command
          (tab seperated 3 columns: reference name, position, depth)
  <threshold>: INT, a depth thrshold, like 100
  OUTPUT: a new depth file with depth above given threshold

AUTHER: ysh_xiong(1240172230@qq.com)"""
    print(message)


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
    print('output depth file at "{}"'.format(out_filename))
    print('{} / {} positions isolated : {}%'.format(new_count, raw_count, trim_percent))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        usage()
    elif len(sys.argv) == 3:
        try:
            main()
            print('done!')
        except:
            usage()
    else:
        usage()
