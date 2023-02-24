import numpy
import pandas


def multi_table(n):
    rows = numpy.arange(0, n+1)
    return rows * rows[:, None]


# main program
a = int(input())
print(pandas.DataFrame(multi_table(a)).to_string(header=True))
