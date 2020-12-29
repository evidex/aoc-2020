from itertools import product


def read_pocket(pocket_path, dimensions):
    pocket = set()

    with open(pocket_path) as initf:
        for y, line in enumerate(initf.readlines()):
            for x, activity in enumerate(line.strip()):
                if activity == '#':
                    # Add the right amount of dimensions
                    cube_pos = (x,y) + (0,)*(dimensions-2)
                    pocket.add(cube_pos)
    return pocket


def print_pocket(pocket, dimensions):
    mins = [min(pos[i] for pos in pocket) for i in range(dimensions)]
    maxs = [max(pos[i] for pos in pocket) for i in range(dimensions)]

    for higher_dims in product(*[range(mins[i], maxs[i]+1) for i in range(2, dimensions)]):
        # Print coordinates of higher dimensions
        print(', '.join(f"d{i}={higher_dims[i]}" for i in range(dimensions - 2)))
        for y in range(mins[1], maxs[1]+1):
            for x in range(mins[0], maxs[0]+1):
                if (x, y, *higher_dims) in pocket:
                    print('#', end='')
                else:
                    print('.', end='')
            print()
        print()


def evolve_pocket(pocket, dimensions, steps, debug=False):
    for cycle in range(steps):

        # Save number of neighbours for all cubes with neighbours
        neighbours = dict()
        for pos in pocket:
            for diffs in product([-1, 0, 1], repeat=dimensions):
                if diffs != (0,)*dimensions:
                    neigh_pos = tuple([i + di for i,di in zip(pos, diffs)])
                    neighbours[neigh_pos] = neighbours.get(neigh_pos, 0) + 1

        # Apply evolution rules based on neighbour count and previous state
        next_pocket = set()
        for neigh_pos, neighbour_count in neighbours.items():
            if (neigh_pos in pocket and neighbour_count == 2) \
                    or neighbour_count == 3:
                next_pocket.add(neigh_pos)

        # Save the next pocket composition
        pocket = next_pocket
        if debug:
            print(f"-------- Cycle {cycle} --------")
            print_pocket(pocket, dimensions)
            input()

    return pocket


if __name__ == '__main__':

    # Part 1
    pocket3d = read_pocket('test-input.txt', 3)

    print("Input:")
    print_pocket(pocket3d, 3)

    pocket3d = evolve_pocket(pocket3d, 3, 6, debug=True)
    print(len(pocket3d))


    # Part 2
    #pocket4d = read_pocket('input', 4)
    #
    #print("Input:")
    #print_pocket(pocket4d, 4)

    #pocket4d = evolve_pocket(pocket4d, 4, 6)
    #print(len(pocket4d))

