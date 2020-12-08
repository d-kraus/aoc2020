def first_part(filepath):
    with open(filepath) as input_file:
        valid_passwords = 0
        for line in input_file:
            line = line.strip()
            (policy, password) = line.split(': ')
            (policy_range, letter) = policy.split(' ')
            (min, max) = policy_range.split('-')
            min = int(min)
            max = int(max)

            occurrences = 0

            for char in password:
                if char == letter:
                    occurrences += 1

            if min <= occurrences <= max:
                valid_passwords += 1

        print('Solution for day 2, part 1')
        print(f'Valid passwords: {valid_passwords}')


def second_part(filepath):
    with open(filepath) as input_file:
        valid_passwords = 0
        for line in input_file:
            line = line.strip()
            (policy, password) = line.split(': ')
            (policy_range, letter) = policy.split(' ')
            (pos_1, pos_2) = policy_range.split('-')
            pos_1 = int(pos_1) - 1
            pos_2 = int(pos_2) - 1

            if (password[pos_1] == letter or password[pos_2] == letter) and password[pos_1] != password[pos_2]:
                valid_passwords += 1

        print('Solution for day 2, part 2')
        print(f'Valid passwords: {valid_passwords}')