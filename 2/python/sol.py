from collections import Counter
from operator import xor
from collections import namedtuple

Password = namedtuple('Password', ('min', 'max', 'elem', 'password'))

passwords = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        policy, password = line.split(':')
        nums, elem = policy.split(' ')
        min_elem, max_elem = nums.split('-')
        passwords.append(Password(int(min_elem), int(max_elem), elem, password.strip()))

def verify_policy(password):
    count = Counter(password.password)
    return password.min <= count[password.elem] <= password.max

def verify_policy2(password):
    first = password.password[password.min-1] == password.elem
    try:
        second = password.password[password.max-1] == password.elem
    except IndexError:
        second = False
    return first != second

def count_policy(passwords, policy):
    return Counter(map(policy, passwords))[True]

test = [
    Password(1, 3, 'z', 'zfo'),
    Password(1, 3, 'z', 'zfz'),
    Password(1, 3, 'e', 'zfz'),
    Password(1, 3, 'z', 'ofz'),
    Password(1, 4, 'z', 'ofz'),
    Password(1, 4, 'z', 'zfz'),
]
assert (count_policy(test, verify_policy)) == 5
assert (count_policy(test, verify_policy2)) == 3

print('Part1 -> ', count_policy(passwords, verify_policy))
print('Part2 -> ', count_policy(passwords, verify_policy2))
