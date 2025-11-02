# Lambda
list1 = [1,2,3,4,5]
cube = list(map(lambda x: x**3, list1))
print(cube)
# for with list comprehension
cube2 = [i**3 for i in list1]
print(cube2)
# for with if & list comprehension
cube2 = [i**3 for i in list1 if i%2==0]
print(cube2)

# Map, Reduce, Filter
from functools import reduce
# Map
list2 = [1,2,3,4,5]
square = list(map(lambda x: x**2, list2))
print(square)
# Filter - acts as for with if
square = list(filter(lambda x: x%2==0, list2))
print(square)
# Reduce - doesn't need list
sum_list = reduce(lambda x,y: x+y, list2)
print(sum_list)

# Higher Order Functions
from typing import Callable, List

even = lambda x:x%2==0
odd = lambda x:x%2!=0
three = lambda x:x%3==0

def higher_order_function(fun: Callable, vec: List):
    result = []
    for item in vec:
        if fun(item):
            result.append(item)
    return result

print(higher_order_function(even,list2))
print(higher_order_function(odd,list2))
print(higher_order_function(three,list2))