#!/usr/bin/env python
#-*-coding:utf-8-*-
def filter():
    file = "F:/waitex/Version/"
    lines, sorted = open(file+"change.txt", 'r').readlines(), lambda a, cmp: a.sort(cmp=cmp) or a
    open(file+"changeFiltered.txt", 'w').write(''.join([l[0] for l in sorted([(l, lines.index(l)) for l in set(lines)], lambda a,b: a[1]-b[1] )]))
