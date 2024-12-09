#!/usr/bin/env python3
import re

with open('input', 'r') as file:
    lines = file.read().splitlines()

pattern = re.compile("([0-9])")
sum = 0
for line in lines:
    matches = pattern.findall(line)
    sum += int(matches[0] + matches[-1])
    print(f"{matches}")
    print(f"{matches[0]}, {matches[-1]}")

print(sum)
