def min_distance(n):
    spis = []
    for d in range(1, n+1):
        if n % d == 0:
            spis.append(d)
    res = spis[-1]
    for i in range(len(spis) - 1):
        res = min(res, abs(spis[i] - spis[i+1]))
    return res