#!/usr/bin/env python3

def parse_line(line, data) -> int:
    card, numbers = line.split(":")
    id = int(card.split(" ")[-1])
    winning, have = numbers.split("|")
    winning = [int(i) for i in winning.split(" ") if i.isdigit()]
    print(f"winning:{winning}")
    have = [int(i) for i in have.split(" ") if i.isdigit()]
    print(f"have:{have}")
    matches = 0
    for n in have:
        if n in winning:
            matches += 1
    data.append({
        "card": id,
        "count": 1,
        "matches": matches
    })

def main(input='input'):

    with open(input, 'r') as file:
        lines = file.read().splitlines()

    data = []
    for line in lines:
        parse_line(line, data)
    for i in range(len(data)):
        for j in range(i + 1,i + 1 + data[i]["matches"]):
            data[j]["count"] += data[i]["count"]

    print(data)
    total_cards = sum([c["count"] for c in data])
    print(f"total cards:{total_cards}")


if __name__ == "__main__":
    main()
    # main('sample')
    # test()


