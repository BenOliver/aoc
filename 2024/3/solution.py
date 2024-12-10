#!/usr/bin/env python3
import re
import pathlib
import os
import re

pattern = re.compile("mul\((?P<a>[0-9]*),(?P<b>[0-9]*)\)")
def get_mul(line):
    ret = pattern.findall(line)
    mul = 0
    for match in ret:
        mul = mul + int(match[0]) * int (match[1])
    return mul

def main():
    input_file = "input.txt"
    # input_file = "sample.txt"

    input = os.path.join(pathlib.Path(__file__).parent.resolve(), input_file)
    with open(input, "r") as file:
        lines = file.read().splitlines()
    total = 0
    for line in lines:
        total += get_mul(line)
    print(total)

if __name__ == "__main__":
    main()