#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from math import *


def simpson(a, b, n, f):
    h = (b - a) / n
    soma = (execf(f, a) + execf(f, b))
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            soma += 2 * execf(f, x)
        else:
            soma += 4 * execf(f, x)
    return (soma * (h / 3))


def execf(f, x=None):
    return eval(f)


if __name__ == '__main__':
    re = simpson(float(sys.argv[1]),
                 float(execf(sys.argv[2])),
                 int(sys.argv[3]),
                 sys.argv[4])
    print(re)
