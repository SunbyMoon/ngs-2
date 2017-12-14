#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_


class read_bs(object):
    def __init__(self, filename):
        self.__location = {}
        with open(filename) as handle:
            for line in handle:
                line = line.strip()
                loci, alleles = line.split('\t')
                self.__location[loci] = eval(alleles)  # alleles is a dict

        self.__homo = {}
        self.__hetero = {}
        for (loci, allele) in self.__location.items():
            if len(allele) == 1:
                # print('homo', loci, allele)
                self.__homo[loci] = allele  # homozygote alleles in a dict
            elif len(allele) > 1:
                # print('hetero', loci, allele)
                self.__hetero[loci] = allele  # heterozygote alleles in a dict

    def all_loci(self):
        return self.__location

    def homo_site(self):
        return self.__homo

    def hetero_site(self):
        return self.__hetero


def main():
    mother = read_bs('PB2017101906M.bs')
    pool = read_bs('PB2017101906POOL.bs')
    count = 0
    for loci, genotype in mother.homo_site().items():
        if loci in pool.hetero_site():
            pool_genotype = pool.hetero_site()[loci]
            count += 1
            print('{}_th informative site:{}, \tmaternal:{}, \tpool:{}'.format(
                count, loci[:30], genotype.keys(), pool_genotype))


if __name__ == '__main__':
    main()
    print('\n- - done! - - \n')
