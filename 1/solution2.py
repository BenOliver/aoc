#!/usr/bin/env python3
import re

pattern = re.compile(".*?([0-9]|one|two|three|four|five|six|seven|eight|nine)")
pattern_greedy = re.compile(".*([0-9]|one|two|three|four|five|six|seven|eight|nine)")


def convert(string) -> int:
    if string.isdigit():
        return int(string)
    elif string == "one":
        return 1
    elif string == "two":
        return 2
    elif string == "three":
        return 3
    elif string == "four":
        return 4
    elif string == "five":
        return 5
    elif string == "six":
        return 6
    elif string == "seven":
        return 7
    elif string == "eight":
        return 8
    elif string == "nine":
        return 9
    return "ERROR"


def parse_line(line) -> int:
    match_first = pattern.match(line).groups()
    match_end = pattern_greedy.match(line).groups()

    # print(f"{line}: {match_first} {match_first}")
    first = convert(match_first[0])
    last = convert(match_end[0])
    # print(f"{line}: {first} {last}")
    return (10 * first) + last


def main(input='input'):

    with open(input, 'r') as file:
        lines = file.read().splitlines()

    sum = 0
    for line in lines:
        ret = parse_line(line)
        # print(f"{line}: {ret}")
        sum += ret

    print(sum)


def test():
    tests = [
        ['onetwothreefour', 14],
        ['2onetwothreefour', 24],
        ['dfeasaednetwothreefour', 24],
        ['nineight5twothreefour', 94],
        ['twonenineight5twothreetwone', 21],
    ]
    for i, test in enumerate(tests):
        outcome = parse_line(test[0])
        if outcome != test[1]:
            print(f"test {i} failed")
            print(f"{test[0]} -> {outcome} != {test[1]}")
        else:
            print(f"test {i} passed")


if __name__ == "__main__":
    main()
    # main('sample')
    # test()
