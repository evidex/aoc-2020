from collections import defaultdict
with open('input.txt', 'r') as f:
    data = f.readlines()

with open('test-input.txt', 'r') as f:
    test_data = f.readlines()



class Conway:
    ACTIVE = '#'
    def __init__(self, data):
        self.data = data
        self.state = defaultdict(list)
        self.parse_data()

    def map_active(self, char):
        return True if char == self.ACTIVE else False

    def parse_data(self):
        for line in self.data:
            self.state[0].append([[self.map_active(c) for c in line.strip()]])


c = Conway(test_data)
