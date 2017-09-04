## Lists (c++ vector)
# Heterogeneous
empty_list = [] # or list()
xs = [1, 2, "3", 4.0]
len(xs) # list length
# xs[i] -- get i-th element
# xs[i] = 2  # assign ith element to 2
# xs[-1] -- last element

# Slicing -- sublist
# xs([start,] stop[, step]) -- general syntax
# xs[:] - copy
# xs[1:] - from 1st element
# xs[:10] - to 10 (not included)
# xs[1:10] - from 1 to 10
# xs[1:10:2] - from 1 to 10 step by 2
# xs[::-1] - in reverse order
# xs[ind1:ind2] = lst2  - replace sublist
# xs.append(el), xs.remove(el), val in xs,
# xs.index(el), xs.count(el), xs.extend(list)
# Multiply lists
# [1,2,3] * 2 == [1,2,3, 1,2,3]
# ys = xs # aliasing
## Copy
#   ys = xs.copy()
#   ys = xs[:]
#   ys = list(xs)
## Sort
# xs.sort() # mutates xs
# xs.sort(reverse=True) # in reverse order
def second(pair):
    return pair[1]
a = [("hello", 2), ("world", 1)]
a.sort(key=second) # sort pairs by second element
a.sort(key=lambda x: x[1]) # same using lambda
# sorted(xs) ## returns new list
# dir([]) - all list methods

### Tuples
# Tuple - immutable list
# empty_tuple = (,)
# singleton = (1,)
# a = (1, 2, 3)
# a[0] = 2 # error
# "Immutable"
# a = ([1,2,3], 4)
# a[0].append(4)
# b = a
# a += (4, 5, 6)
# b != a
