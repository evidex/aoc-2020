with open('input.txt', 'r') as f:
    data = f.readlines()

test_data = ['abc', '\n', 'a\n', 'b\n', 'c\n', '\n', 'ab\n', 'ac\n', '\n', 'a\n', 'a\n', 'a\n', 'a\n', '\n', 'b\n']

def get_groups(data):
    groups = []
    group = []
    for line in data:
        answers = line.strip()
        if answers:
            group.append(set(answers))
        else:
            groups.append(group)
            group = []
    groups.append(group)
    return groups

def get_all_answers(data):
    groups = get_groups(data)
    return sum([len(set.union(*g)) for g in groups])

def get_common_answers(data):
    groups = get_groups(data)
    return sum([len(set.intersection(*g)) for g in groups])

assert len(get_groups(test_data)) == 5
assert len(get_groups(test_data)[0]) == 1
assert len(get_groups(test_data)[0][0]) == 3

part1 = get_all_answers(data)
assert part1 < 6644
assert part1 == 6630
print(f'Part1 -> {part1}')

#Part 2
part2 = get_common_answers(data)
assert part2 < 3501
print(f'Part2 -> {part2}')

