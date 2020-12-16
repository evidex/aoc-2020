import time
treemap = []
TREE = '#'
with open('input.txt', 'r') as f:
    for line in f.readlines():
        treemap.append([c == TREE for c in line.strip()])


def count_trees(treemap, down, right):
    # count 1d 3r
    count = 0
    pos = (0,0) #row, col
    width = len(treemap[0])
    while pos[0] < len(treemap):
        if treemap[pos[0]][pos[1]]:
            count += 1
        pos = (pos[0]+down, (pos[1]+right)%width)
    return count


# Part1
start = time.time()
part1 = count_trees(treemap, 1, 3)
time_taken = time.time() - start
assert part1 <= len(treemap)
assert part1 == 294
print(f'Part 1 - {part1} in {time_taken}s')

# Part2
vectors = [(1,1), (1,3), (1,5), (1,7), (2,1)]
start = time.time()
part2= 1
res = [count_trees(treemap, d, r) for d,r in vectors]
print(res)
for elem in res:
    part2 = part2 * elem

assert res[1] == 294

time_taken = time.time() - start
print(f'Part 2 - {part2} in {time_taken}s')
