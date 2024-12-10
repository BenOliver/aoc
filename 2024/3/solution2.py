#!/usr/bin/env python3
import re
import pathlib
import os
import re

pattern = re.compile("mul\((?P<a>[0-9]*)\,(?P<b>[0-9]*)\)|(?P<do>do\(\))|(?P<dont>don't\(\))")
def get_mul(line):
    # ret = pattern.findall(line)
    matches = [m.groupdict() for m in pattern.finditer(line)]
    mul = 0
    do = True
    for match in matches:
        if match["dont"]:
            do = False
        if match["do"]:
            do = True
        if do and match["a"]:
            mul = mul + int(match["a"]) * int(match["b"])
    return mul

def main():
    input_file = "input.txt"
    # input_file = "sample.txt"

    input = os.path.join(pathlib.Path(__file__).parent.resolve(), input_file)
    with open(input, "r") as file:
        lines = file.read()
    total = 0
    # for line in lines:
    total += get_mul(lines)
    print(total)

if __name__ == "__main__":
    main()