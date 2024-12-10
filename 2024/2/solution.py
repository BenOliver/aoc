#!/usr/bin/env python3
import re
import pathlib
import os



def check_safe(line):
    line = [int(i) for i in line.split()]
    print(line)
    i = line[0]
    diff = []
    for j in line[1:]:
        diff.append(j-i)
        i = j
    print(diff)
    pos = True if diff[0] > 0 else False
    if pos:
        for i in diff:
            if i < 0:
                print(f"unsafe, change of sign")
                return 0
    else:
        for i in diff:
            if i > 0:
                print(f"unsafe, change of sign")
                return 0
    for d in diff:
        if d not in [1, 2, 3, -1, -2, -3]:
            print(f"unsafe: change of {d}")
            return 0
    print("safe")
    return 1

def main():
    input_file = "input.txt"
    # input_file = "sample.txt"

    input = os.path.join(pathlib.Path(__file__).parent.resolve(), input_file)
    with open(input, "r") as file:
        lines = file.read().splitlines()
    safe = 0
    for line in lines:
        safe += check_safe(line)
    print(safe)

if __name__ == "__main__":
    main()