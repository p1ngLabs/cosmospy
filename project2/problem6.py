def get_min_max(ints):
  """
  Return a tuple(min, max) out of list of unsorted integers.
  Expected time complexity: O(n)
  
  Args:
      ints(list): list of integers containing one or more integers
  """
  if not ints or len(ints) == 0:
    return None, None
    
  min = max = ints[0]
    
  for num in ints:
    if type(num) is not int:
      return None, None

    if num < min: min = num
    elif num > max: max = num
    
  return min, max


# Test Case 1: Sanity test
print ("Pass" if ((1, 9) == get_min_max([2, 7, 3, 6, 4, 1, 9, 8, 5])) else "Fail")

# Test Case 2: Empty list
print("Pass" if ((None, None) == get_min_max([])) else "Fail")

# Test Case 3: None as input
print("Pass" if ((None, None) == get_min_max(None)) else "Fail")

# Test Case 4: List element is not integer
print("Pass" if ((None, None) == get_min_max([12, "test", 34])) else "Fail")
