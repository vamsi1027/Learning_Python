# map, filter, zip, and reduce, lambad
# lambad param:function(paramter)
from functools import reduce

import self as self

new_array_list = [1, 2, 3, 4]

old_array_list = [10, 20, 30]

update_array_list = [5, 6, 7, 8]


def multiple_by_2(iterable):
    # list_value = []
    # for items in iterable:
    #   list_value.append(items * 2)
    return iterable * 2


def check_even(iterable):
    return iterable % 2 != 0


def accumulated(acc, items):
    print(acc, items)
    return acc + items


result_map = list(map(multiple_by_2, new_array_list))
print(result_map)

result_filter = list(filter(check_even, new_array_list))
print(result_filter)

result_zip = list(zip(new_array_list, old_array_list, update_array_list))
print(result_zip)

result_reduce = reduce(accumulated, new_array_list, 0)
print(result_reduce)

# Same way for filter, zip, reduce
result_lambda = list(map(lambda iteams: iteams * 2, new_array_list))
print(result_lambda)

# Square

result_square = list(map(lambda iteamOne: iteamOne ** 2, new_array_list))
print(result_square)

list_value = [(1, 3), (2, 4), (10, -1)]
list_value.sort()
print(list_value)
list_value.sort(key=lambda x: x[1])
print(list_value)


def generate(self, value):
    print(value)
    print(self)


def another_generate(self, value):
    generate(self, value)


another_generate(self, 1)
