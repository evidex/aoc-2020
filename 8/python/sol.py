with open('input.txt', 'r') as f:
    data = f.readlines()

class GameBoy:
    def __init__(self, source):
        self.source = source

    def run(self, source):
        acc = 0
        pointer = 0
        processed = []
        while True:
            if pointer in processed:
                print(f'Breaking at pointer {pointer} due to loop')
                return False, acc
                break
            else:
                processed.append(pointer)

            try:
                line = source[pointer]
            except IndexError:
                break
            op, value = line.split(' ')
            value = int(value)

            if op == 'acc':
                acc += value
            elif op == 'jmp':
                pointer += value
                continue
            pointer += 1
        return True, acc

    def find_halt(self):
        return self.run(self.source)

    def find_non_halting(self):
        for cand_pointer, _ in enumerate(self.source):
            op, value = self.source[cand_pointer].split(' ')
            if op == 'acc':
                continue
            else:
                source = self.source.copy()
                op = 'jmp' if op == 'nop' else 'nop'
                source[cand_pointer] = f'{op} {value}'
                no_halt , acc = self.run(source)
                if no_halt:
                    print(f'Finished at cand {cand_pointer}')
                    return acc
                    break



test_data = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.split('\n')

gb = GameBoy(test_data)
#_, res = gb.find_halt()
#print(f'Test halts -> {res}')
#assert res == 5
res = gb.find_non_halting()
print(f'Test non halts -> {res}')
assert res == 8


gb = GameBoy(data)
_, res = gb.find_halt()
assert res == 1939
print(f'Part1 -> {res}')

gb = GameBoy(data)
res = gb.find_non_halting()
print(f'Part2 -> {res}')

