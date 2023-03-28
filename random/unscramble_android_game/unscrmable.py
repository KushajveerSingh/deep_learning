from itertools import combinations, permutations
from collections import defaultdict
import sys
import enchant
dictionary = enchant.Dict("en_us")

def get_subs(s:str):
    """
    get_subs('abc')
    {'ab', 'abc', 'ac', 'acb', 'ba', 'bac', 'bc', 'bca', 'ca', 'cab', 'cb', 'cba'}
    """
    return set([''.join(p) for r in range(2, len(s)+1) for p in permutations(s, r)])

def check_subs(subs:set):
    """
    check_subs(get_subs('abc'))
    ['ac', 'cab', 'ab', 'ca']
    """
    valid_subs = []
    for sub in subs:
        if dictionary.check(sub): valid_subs.append(sub)
    return valid_subs

def print_subs(valid_subs:list):
    """
    Words of length 2
    ab
    ac
    ca

    Words of length 3
    cab
    """
    max_len = -1
    for sub in valid_subs:
        if len(sub) > max_len: max_len = len(sub)
    
    output = [[] for _ in range(max_len)]
    for sub in valid_subs: output[len(sub)-1].append(sub)
    
    for i in range(len(output)): output[i].sort()
        
    for i, o in enumerate(output):
        if len(o) == 0: continue
        
        print(f'Words of length {i+1}')
        for o_ in o: print(f'{o_}')
        print()

def unscramble(s:str):
    subs = get_subs(s)
    valid_subs = check_subs(subs)
    print_subs(valid_subs)


if __name__ == '__main__':
    letters = str(sys.argv[1])
    unscramble(letters)