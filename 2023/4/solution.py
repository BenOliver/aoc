#!/usr/bin/env python3

def parse_line(line) -> int:
    card, numbers = line.split(":")
    winning, have = numbers.split("|")
    winning = [int(i) for i in winning.split(" ") if i.isdigit()]
    print(f"winning:{winning}")
    have = [int(i) for i in have.split(" ") if i.isdigit()]
    print(f"have:{have}")
    score = 0.5
    for n in have:
        if n in winning:
            score *= 2
    if score == 0.5:
        return 0
    return int(score)

def main(input='input'):

    with open(input, 'r') as file:
        lines = file.read().splitlines()

    sum = 0
    for line in lines:
        ret = parse_line(line)
        # print(f"{line}: {ret}")
        sum += ret

    print(sum)


if __name__ == "__main__":
    main()
    # main('sample')
    # test()


