def even_filter(nums_list):
    return [i for i in nums_list if i % 2 == 0]


print(even_filter([1, 2, 3, 4, 5, 6, 7]))


# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))

