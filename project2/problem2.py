def rotated_array_search(input_list, number):
  """
  Find the index by searching in a rotated sorted array
  Expected time complexity: O(logn)

  Args:
      input_list(array), number(int): Input array to search and the target
  Returns:
      int: Index or -1
  """
  start, end = 0, len(input_list) - 1
    
  while start <= end:
    middle = (start + end) // 2

    if input_list[middle] == number:
      return middle

    # check if start half is sorted
    if input_list[start] <= input_list[middle]:
      if input_list[start] <= number < input_list[middle]:
        end = middle - 1
      else:
        start = middle + 1

    # check if the right half is sorted
    else:
      if input_list[middle] < number <= input_list[end]:
        start = middle + 1
      else:
        end = middle - 1

  return -1

def linear_search(input_list, number):
  for index, element in enumerate(input_list):
    if element == number:
        return index
  return -1
    
def test_function(test_case):
  input_list = test_case[0]
  number = test_case[1]
  if linear_search(input_list, number) == rotated_array_search(input_list, number):
    print("Pass")
  else:
    print("Fail")

# Test Case 1: Sanity test
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# should all print "Pass"

# Test Case 2: Empty array
test_function([[], 5])
# both search algorithm returns -1

# Test Case 3: Sorted array
test_function([[1,2,3,4,5,6,7,8,9], 10])
test_function([[1,2,3,4,5,6,7,8,9], 6])
