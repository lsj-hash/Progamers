import math

def solution(a, b):

    gcd_ab = math.gcd(a, b)
    b //= gcd_ab 
    for p in [2, 5]:
        while b % p == 0:
            b //= p

    return 1 if b == 1 else 2
