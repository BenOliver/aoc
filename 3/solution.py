#!/usr/bin/env python3


def parse_symbol(y_origin, x_origin, grid) -> int:
    sum = 0
    for y in y_origin - 1, y_origin, y_origin + 1:
        for x in x_origin - 1, x_origin, x_origin + 1:
            if grid[y][x].isdigit():
                # print(f"digit found at {y},{x}")
                num_str = grid[y][x]
                grid[y][x] = "."
                for i in range(x+1, len(grid[y])):
                    if grid[y][i].isdigit():
                        # print(f"{i} is digit")
                        num_str += grid[y][i]
                        grid[y][i] = "."
                    else:
                        # print(f"{i} not digit")
                        break

                for i in range(x-1, -1, -1):
                    if grid[y][i].isdigit():
                        # print(f"{i} is digit")
                        num_str = grid[y][i] + num_str
                        grid[y][i] = "."
                    else:
                        # print(f"{i} not digit")
                        break
                print(f"Found number {num_str}")
                sum += int(num_str)
    return sum
    

def main(input='input'):

    with open(input, 'r') as file:
        lines = file.read().splitlines()

    sum = 0
    grid = []
    for line in lines:
        grid.append([i for i in line])
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char not in "0123456789.":
                print(f"processing symbol at {y},{x}")
                # is a symbol, add to sum
                sum += parse_symbol(y, x, grid)
            
    print(sum)


if __name__ == "__main__":
    main()
    # main('sample')
    # test()


