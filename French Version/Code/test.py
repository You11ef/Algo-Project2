#!/usr/bin/env python3

from timeit import timeit
from sys import argv

from geo.point import Point
from connectes import print_components_sizes, load_instance
from connectes_amel import print_components_sizes_amel
import matplotlib.pyplot as plt
import sys
import os
from time import time
from generator import gen



def testing(n):

    x = [i*50 for i in range(10, n+1)]
    y2 = []
    y1 = []
    for i in x:
        gen(i)
        distance, points = load_instance(f"exemple_{i}.pts")
        pointss = points[:]
        begin1 = time()
        print_components_sizes(distance, points)
        y1.append(time()-begin1)
        begin2 = time()
        print_components_sizes_amel(distance, pointss)
        y2.append(time()-begin2)
        os.system(f"rm exemple_{i}.pts")
    plt.plot(x, y1, label="old")
    plt.plot(x, y2, label="new")
    plt.legend()
    plt.show()


def main():
    testing(int(sys.argv[1]))

if __name__ == "__main__":
    main()
