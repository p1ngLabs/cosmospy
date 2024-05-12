def sqrt(number):
  """
  Calculate the floored square root of a number
  Expected time complexity: O(logn)

  Args:
    number(int): Number to find the floored squared root
  Returns:
    int: Floored Square Root
  """
  if number == 0 or number == 1:
    return number

  start, end = 1, number
  result = 0

  while start <= end:
    middle = (start + end) // 2

    if middle ** 2 <= number:
      result = middle
      start = middle + 1
    else:
      end = middle - 1

  return result


# Test Case 1: Sanity test
print(sqrt(16), sqrt(36), sqrt(100))
# prints 4, 6, 10

# Test Case 2: Given number is 0 or 1
print(sqrt(0), sqrt(1))
# prints 0 and 1

# Test Case 3: Return floored value of given number
print(sqrt(5), sqrt(27))
# prints 2, 5
