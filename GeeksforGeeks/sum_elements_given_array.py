from functools import reduce

def sum_array(arr):
  return reduce(lambda x, y: x + y, arr)

arr = [12, 3, 4, 15]
print("Sum of given array is", sum_array(arr))