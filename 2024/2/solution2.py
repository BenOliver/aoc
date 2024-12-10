#!/usr/bin/env python3
import re
import pathlib
import os
from copy import deepcopy


def check_safe(line, remove=None):
    if isinstance(line, str):
        original_line = [int(i) for i in line.split()]
        line = [int(i) for i in line.split()]
    else:
        original_line = deepcopy(line)
    if remove != None:
        if remove >= len(original_line):
            print(original_line)
            print(line)
            print(f"all removals exhausted")
            return 0
        del line[remove]
        remove += 1
    else:
        remove = 0

    # print(line)
    i = line[0]
    diff = []
    for j in line[1:]:
        diff.append(j-i)
        i = j
    # print(diff)
    pos = True if diff[0] > 0 else False
    if pos:
        for i in diff:
            if i < 0:
                # print(f"unsafe, change of sign")
                return check_safe(original_line, remove)
    else:
        for i in diff:
            if i > 0:
                # print(f"unsafe, change of sign")
                return check_safe(original_line, remove)
    for d in diff:
        if d not in [1, 2, 3, -1, -2, -3]:
            # print(f"unsafe: change of {d}")
            return check_safe(original_line, remove)
    return 1

def main():
    input_file = "input.txt"
    # input_file = "sample.txt"
    # input_file = "sample2.txt"

    input = os.path.join(pathlib.Path(__file__).parent.resolve(), input_file)
    with open(input, "r") as file:
        lines = file.read().splitlines()
    safe = 0
    for line in lines:
        safe += check_safe(line)
    print(safe)

if __name__ == "__main__":
    main()