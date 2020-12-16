with open('input.txt', 'r') as f:
    passes = [l.strip() for l in f.readlines()]

MAX_ROW = 127
MAX_SEAT = 7

def bsp(pattern, max_pos, min_pos=0):
    c = pattern[0]
    if len(pattern) == 1:
        return min_pos if c in ['L', 'F'] else max_pos
    elif c == 'F' or c == 'L':
        max_pos = min_pos + (max_pos - min_pos) // 2
    else:
        min_pos = 1 + min_pos + ((max_pos - min_pos) // 2)
    return bsp(pattern[1:], min_pos=min_pos, max_pos=max_pos)

row = bsp('FBFBBFF', MAX_ROW)
seat = bsp('RLR', MAX_SEAT)
assert row == 44
assert seat == 5

def get_id(row, seat):
    return (row * 8) + seat

assert get_id(row, seat) == 357

def parse_passes(passes):
    return [get_id(bsp(bpass[:7], MAX_ROW), bsp(bpass[7:], MAX_SEAT)) for bpass in passes]

print(f'Part1 -> {max(parse_passes(passes))}')

def print_plane(passes):
    seat_ids = parse_passes(passes)
    for seat in range(MAX_SEAT+1):
        for row in range(MAX_ROW+1):
            c = '.' if get_id(row, seat) not in seat_ids else '#'
            print(c, end='')
        print('')

print_plane(passes)

# 74 5
# 597

def find_my_seat(passes):
    seat_ids = sorted(parse_passes(passes))
    for p, n in zip(seat_ids, seat_ids[1:]):
        if n-p > 1:
            return p+1

print(f'Part2 -> {find_my_seat(passes)}')
