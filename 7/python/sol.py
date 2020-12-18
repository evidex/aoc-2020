import re

class RuleParser():
    def __init__(self, rule_data):
        self.rule_data = rule_data
        self.bags = {}
        self.parse_rules()

    def parse_rules(self):
        for line in self.rule_data:
            colour, _, contains = line.partition('bags')
            colour = colour.strip().lower()
            contains = re.findall(r'\d.+?(?=bag)', contains)
            self.bags[colour] = {}
            for bag_desc in contains:
                limit, _, bag_colour = bag_desc.strip().partition(' ')
                bag_colour = bag_colour.strip().lower()
                limit = int(limit.strip())
                self.bags[colour].update({bag_colour: limit})

    def find_colour(self, bag, colour):
        return colour in bag or\
                any(self.find_colour(self.bags.get(b, {}), colour) for b in bag)

    def find_num_paths(self, colour):
        '''Find the number of bags which can contain a bag of a given colour'''
        colour = colour.lower()
        return sum(map(int, [self.find_colour(bag, colour) for _, bag in self.bags.items()]))

    def find_bag_cost(self, colour, c=0):
        '''find_bag_cost -> Find the total number of bags contained within a given colour.

        :param colour:  str - colour to find
        :param c:       int - set to 0 to not include the outer bag in the cost
        '''
        bag = self.bags[colour]
        if not bag:
            return 1
        else:
            return sum([num * self.find_bag_cost(b, c=1) for b, num in bag.items()]) + c

with open('input.txt', 'r') as f:
    data = f.readlines()

parser = RuleParser(data)
colour = 'shiny gold'
print(f'Part1 -> {parser.find_num_paths(colour)} bags for {colour}')
print(f'Part2 -> {parser.find_bag_cost(colour)} bags contained for {colour}')


test_data = '''burnt blue bags contain 4 grank green bags, 1 purple nurple bag.
purple nurple bags contain 2 rocket red bags.
rocket red bags contain no other bags.
grank green bags contain 5 purple nurple bags.
something orange bags contain no other bags.'''.split('\n')

test_data2 = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''.split('\n')

test_parser = RuleParser(test_data)
test_parser.parse_rules()
assert test_parser.find_num_paths('rocket red') == 3
print(test_parser.find_bag_cost('burnt blue'))
assert test_parser.find_bag_cost('burnt blue') == 67

test_parser2 = RuleParser(test_data2)
pprint(test_parser2.bags)
print(test_parser2.find_bag_cost('shiny gold'))
assert test_parser2.find_bag_cost('shiny gold') == 126

