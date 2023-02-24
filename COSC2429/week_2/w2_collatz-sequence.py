def collatz_seq(n):
    """

    :param n: an integer
    :return: seq created by the number
    """
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            seq.append(n)
        else:
            n = n * 3 + 1
            seq.append(n)
    return seq


for i in range(1, 101):
    print(i, " : ", len(collatz_seq(i)))
