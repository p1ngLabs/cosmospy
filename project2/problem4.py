def sort_012(input_list):
  """
  Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
  Expected time complexity: O(n)

  Args:
    input_list(list): List to be sorted
  """
  red, white, blue = 0, 0, len(input_list) - 1
    
  # Single array traversal
  while white <= blue:
    if input_list[white] == 0:
      input_list[red], input_list[white] = input_list[white], input_list[red]
      red += 1
      white += 1
    elif input_list[white] == 1:
      white += 1
    else:
      input_list[white], input_list[blue] = input_list[blue], input_list[white]
      blue -= 1
  
  return input_list

def test_function(test_case):
  sorted_array = sort_012(test_case)
  print(sorted_array)
  if sorted_array == sorted(test_case):
    print("Pass")
  else:
    print("Fail")


# Test Case 1: Sanity test
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Test Case 2: Empty list
test_function([])

# Test Case 3: Input list with a single element
test_function([2])
test_function([0])
