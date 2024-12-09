#!/usr/bin/env python3


def parse_symbol(y_origin, x_origin, grid) -> int:
    product = 1
    num_count = 0
    visited_coords = []
    max_len = len(grid[0]) - 1
    max_height = len(grid) - 1
    for y in max(0, y_origin - 1), y_origin, min(max_height, y_origin + 1):
        for x in max(0, x_origin - 1), x_origin, min(max_len, x_origin + 1):
            if grid[y][x].isdigit():
                if (y, x) in visited_coords:
                    print(f"skipping {y},{x}")
                    continue
                visited_coords.append((y, x))
                if num_count == 2:
                    print(f"too many numbers")
                    return 0
                # print(f"digit found at {y},{x}")
                num_str = grid[y][x]
                # grid[y][x] = "."
                for i in range(x+1, len(grid[y])):
                    if (y, i) in visited_coords:
                        break
                    visited_coords.append((y, i))
                    if grid[y][i].isdigit():
                        # print(f"{i} is digit")
                        num_str += grid[y][i]
                        # grid[y][i] = "."
                    else:
                        # print(f"{i} not digit")
                        break

                for i in range(x-1, -1, -1):
                    if (y, i) in visited_coords:
                        break
                    visited_coords.append((y, i))
                    if grid[y][i].isdigit():
                        # print(f"{i} is digit")
                        num_str = grid[y][i] + num_str
                        # grid[y][i] = "."
                    else:
                        # print(f"{i} not digit")
                        break
                print(f"Found number {num_str}")
                product *= int(num_str)
                num_count += 1

    if num_count == 2:
        print(f"returning {product}")
        return product
    else:
        print(f"num_count is {num_count}")
        return 0
    

def main(input='input'):

    with open(input, 'r') as file:
        lines = file.read().splitlines()

    sum = 0
    grid = []
    for line in lines:
        grid.append([i for i in line])
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "*":
                print(f"processing symbol at {y},{x}")
                # is a symbol, add to sum
                sum += parse_symbol(y, x, grid)
            
    print(sum)


if __name__ == "__main__":
    # main()
    # main('sample')
    main('test1')
    # test()


