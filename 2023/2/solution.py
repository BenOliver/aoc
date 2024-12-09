#!/usr/bin/env python3

def parse_line(line) -> int:
    cubes = {
        "blue": [],
        "red": [],
        "green": [],
    }
    game_num, game = line.split(":")
    sets = game.split(";")
    for set in sets:
        colors = set.split(",")
        for count_color in colors:
            count, color = count_color.strip().split(" ")
            cubes[color].append(int(count))

    blue_max = max(cubes['blue'])
    red_max = max(cubes['red'])
    green_max = max(cubes['green'])
    if all([blue_max <= 14, red_max <= 12, green_max <= 13]):
        print(f"{game_num} is possible")
        return int(game_num.split(" ")[1])
    else:
        print(f"{game_num} is not possible")
        return 0


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


