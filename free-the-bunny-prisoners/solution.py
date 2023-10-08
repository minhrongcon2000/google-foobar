from itertools import combinations

def solution(num_buns, num_required):
    num_copies = num_buns - num_required + 1
    
    bunny2keys = [[] for _ in range(num_buns)]
    
    for key, bunnies in enumerate(combinations(range(num_buns), num_copies)):
        for bunny in bunnies:
            bunny2keys[bunny].append(key)
            
    return bunny2keys
