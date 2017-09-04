# range([start,] stop[, step])
# syntax is same as for ranges
# for i in range(10):
#     print(i)
# for i in range(1, 10, 2):
#     pass
# list comprehensions
# C++:
# int result[100];
# for (int i = 0; i < 100; i++)
#     result[i] = i * i;

# Python:
# [x * x for x in range(100)]
# General syntax:
# [f(i) for i in list if condition]
# python3 range does not create a list (O(1) memory)
# To create a list: list(range(100))

## for-each
# for var in sequence: # sequence is iterable
#   pass
