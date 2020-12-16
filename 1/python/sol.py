import time
with open('input.txt', 'r') as f:
    data = [int(l) for l in f.readlines()]

#part 1
def find2(target):
    for elem in data:
        pair = target-elem
        if pair in data:
            return pair * elem

start = time.time()
print(f'{find2(2020)} - took {time.time()-start}')

def find3(target):
    for elem in data:
        pair = find2(target-elem)
        if pair:
            return pair*elem

start = time.time()
print(f'{find3(2020)} - took {time.time()-start}')
