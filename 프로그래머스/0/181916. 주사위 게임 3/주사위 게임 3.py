from collections import Counter

def solution(a, b, c, d):
    dice = [a, b, c, d]
    count = Counter(dice)
    vals = list(count.values())
    keys = list(count.keys())

    if 4 in vals:
        return 1111 * keys[vals.index(4)]
    elif 3 in vals:
        p = keys[vals.index(3)]
        q = keys[vals.index(1)]
        return (10 * p + q) ** 2
    elif vals.count(2) == 2:
        p, q = keys
        return (p + q) * abs(p - q)
    elif 2 in vals:
        p = keys[vals.index(2)]
        q, r = [k for k in keys if k != p]
        return q * r
    else:
        return min(dice)
