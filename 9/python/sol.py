with open('input.txt', 'r') as f:
    data = f.readlines()
with open('test-input.txt', 'r') as f:
    test_data = f.readlines()


class Xmas:
    PREAMBLE_LENGTH = 25
    def __init__(self, series):
        self.series = [int(c.strip()) for c in series]

    def isvalid(self, pos):
        start = pos - self.PREAMBLE_LENGTH
        pre = self.series[start:pos]
        for a in pre:
            for b in pre:
                if a != b and a+b == self.series[pos]:
                    return True

    def find_first_invalid(self):
        for pos, value in enumerate(self.series[self.PREAMBLE_LENGTH:]):
            if not self.isvalid(pos+self.PREAMBLE_LENGTH):
                return value

    def find_enc_weakness(self, debug=False):
        target = self.find_first_invalid()
        start, end = None, None
        for start_point, a in enumerate(self.series):
            cur = a
            if debug:
                print(f'\n{start_point}: {cur}', end='')
            for end_point, b in enumerate(self.series[start_point+1:]):
                cur += b
                if debug:
                    print(f'+{b}', end='')
                if cur == target:
                    start, end = start_point, end_point+start_point+2
                    break
                if cur > target:
                    if debug:
                        print(f'={cur}', end='')
                    break
            if start or end:
                if debug:
                    print(f'={cur} | {start}-{end}', end='')
                break
        sub_series = sorted(self.series[start:end])
        return sub_series[0] + sub_series[-1]


# Test
xmas = Xmas(test_data)
xmas.PREAMBLE_LENGTH = 5
res = xmas.find_first_invalid()
assert res == 127
res = xmas.find_enc_weakness(debug=True)
assert res == 15+47


# Part 1
xmas = Xmas(data)
res = xmas.find_first_invalid()
assert res == 393911906
# Part 2
res = xmas.find_enc_weakness()
print(res)
assert res == 59341885
