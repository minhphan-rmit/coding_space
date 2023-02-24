def pm(start, end):
    print(start, "->", end)


def tower_of_hanoi(n, start, end):
    if n == 1:
        pm(start, end)
    else:
        other = 6 - (start + end)
        tower_of_hanoi(n - 1, start, other)
        pm(start, end)
        tower_of_hanoi(n - 1, other, end)


print(tower_of_hanoi(8, 1, 3))
