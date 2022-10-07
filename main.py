import random
from time import time


def option():
    print("\t1. First task.\n\t2. Second task.\n\t3. Third task.\n\t0. Exit")
    ch = input("\n>>  ")
    return int(ch)


def first_task():
    i = 8
    while i <= 4096:
        print(f"\nKey length {i} bit - key space {2 ** i}")
        i *= 2
    print()


def second_task():
    i = 8
    keys = {}
    while i <= 4096:
        keys[i] = random.randint(0, 2 ** i)
        print(f"\nGenerated key ({i} bit) - {hex(keys[i])}")
        i *= 2
    print()
    return keys


def third(keys):
    for key in keys:
        start_time = time()
        i = 0
        while i != keys[key]:
            i += 1
        print(f"\n{i} = {hex(keys[key])}, found in {int((time() - start_time) * 1000)} ms")


while 1:
    i = option()
    if i == 1:
        first_task()
    elif i == 2:
        keys = second_task()
    elif i == 0:
        exit()
    else:
        try:
            third(keys)
        except:
            print("\nKeys need to be generated first (2)\n")
