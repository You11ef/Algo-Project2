#! /usr/bin/env python3

import random
from sys import argv



def gen(n):
    with open(f"exemple_{n}.pts", "w") as f:
        dots = [f"{random.random()}, {random.random()}\n" for _ in range(int(n))]
        f.writelines([f"{random.random()}\n"] + dots)

def main():
    n = argv[1]
    gen(n)

if __name__ == "__main__":
    main()