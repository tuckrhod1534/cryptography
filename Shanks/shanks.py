import math
import numpy as np

def get_order(root: int, mod: int):
    for i in range(1, mod):
        if root**i % mod == 1:
            return i
        
def get_inverse(num: int, mod: int):
    num %= mod
    if math.gcd(num, mod) == 1:
        for i in range(1, mod):
            if (num * i) % mod == 1:
                return i
    else:
        return None

def baby_step_giant_step(root: int, mod: int, result: int):
    order = get_order(root, mod)
    if order:
        ## Step 1: Calculate n
        n = 1 + math.floor(np.sqrt(order))
        ## Step 2: Create the lists of powers
        list_a = [(root**pow) % mod for pow in range(n+1)]
        list_b = [(result*get_inverse((root**(k*n)), mod)) % mod for k in range(n+1)]
        print(list_b)
        ## Step 3: Find a match between the two lists
        match = next(iter(set(list_a) & set(list_b)))
        ## Step 4: Return the solution
        if match:
            return (list_a.index(match) + list_b.index(match)*n) % (mod-1)
        else:
            return None