#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_


import sys


def usage():
    message = """a python stript to convert samtools depth output to .bed file
USAGE: python3 depth_2_bed.py <depth_file>
    <depth_file>: output of samtools depth command
Output: a .bed file

AUTHER: ysh_xiong"""
    print(message)


def main():
    dep_filename = sys.argv[1]
    bed_filename = dep_filename + '.bed'
    bed_block_count = 0
    with open(bed_filename, 'w') as bed_handle:
        with open(dep_filename, 'r') as dep_handle:
            first_line = dep_handle.readline().strip()
            [last_ref, pos] = first_line.split()[:2]
            last_pos = int(pos)
            head_pos = int(pos)
            # to initiate position searching
            for line in dep_handle:
                line = line.strip()
                current_ref = line.split()[0]
                current_pos = int(line.split()[1])
                if current_ref == last_ref:   # in the same chromosome
                    if current_pos == last_pos + 1:  # connected position
                        last_pos = current_pos
                    elif current_pos > last_pos:
                        # not connected, come to next block
                        # first, write last block
                        # Importent: .bed file is 0-based and half included
                        # eg. first 100 bases is 0-100
                        bed_block = '{}\t{}\t{}\n'.format(current_ref, head_pos - 1, last_pos)
                        bed_handle.write(bed_block)
                        # print('1', bed_block.strip())
                        bed_block_count += 1
                        head_pos = current_pos
                        last_pos = current_pos
                else:   # jump to next chromosome
                        # write last block
                    bed_block = '{}\t{}\t{}\n'.format(last_ref, head_pos - 1, last_pos)
                    bed_handle.write(bed_block)
                    # print('2', bed_block.strip())
                    bed_block_count += 1
                    last_ref = current_ref
                    last_pos = current_pos
                    head_pos = current_pos
            # reaching to the end of file
            # write last block
            bed_tail_block = '{}\t{}\t{}'.format(current_ref, head_pos - 1, last_pos)
            bed_handle.write(bed_tail_block)
            # print('3', bed_tail_block.strip())
            bed_block_count += 1
    # main job done
    print('\n{} bed blocks writen to file:\n\t"{}"\n'.format(bed_block_count, bed_filename))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            main()
            print('done!')
        except:
            usage()
    else:
        usage()
