from itertools import combinations


def parse_input(filepath):
    parsed = []
    with open(filepath) as input_file:
        for line in input_file:
            trimmed = line.strip()
            numeral = int(trimmed)
            parsed.append(numeral)

    return parsed


def first_part(filepath):
    numbers = parse_input(filepath)
    for (a, b) in combinations(numbers, 2):
        if a + b == 2020:
            print(f'Solution for day 1')
            print(f'{a} + {b} = 2020, {a} * {b} = {a * b}')
            break


def second_part(filepath):
    numbers = parse_input(filepath)
    for (a, b, c) in combinations(numbers, 3):
        if a + b + c == 2020:
            print(f'Solution for day 1, part 2')
            print(f'{a} + {b} + {c} = 2020, {a} * {b}  * {c} = {a * b * c}')
            break
