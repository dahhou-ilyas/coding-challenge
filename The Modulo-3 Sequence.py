def find_nth_number(n):
    sequence = [0, 1, 1, 2, 0, 2, 2, 1]
    return sequence[(n - 1) % 8]

print(find_nth_number(1000000000))