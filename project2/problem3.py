def rearrange_digits(input_list):
  """
  Rearrange Array Elements so as to form two number such that their sum is maximum.
  Expected time complexity: O(nlogn)

  Args:
    input_list(list): Input List
  Returns:
    (int),(int): Two maximum sums
  """
  if len(input_list) <= 1: return input_list

  for i in input_list:
    if type(i) is not int or i not in range(10):
      return [0, 0]
  
  sorted_list = merge_sort(input_list)
  
  num1 = 0
  num2 = 0
  
  # Alternate between adding digits to num1 and num2
  for i in range(len(sorted_list)):
    if i % 2 == 0:
      num1 = num1 * 10 + sorted_list[i]
    else:
      num2 = num2 * 10 + sorted_list[i]
  
  return [num1, num2]

def merge_sort(arr):
  if len(arr) <= 1: return arr
  
  mid = len(arr) // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])
  
  return merge(left, right)

def merge(left, right):
  result = []
  left_index = 0
  right_index = 0
  
  while left_index < len(left) and right_index < len(right):
    if left[left_index] > right[right_index]:
      result.append(left[left_index])
      left_index += 1
    else:
      result.append(right[right_index])
      right_index += 1
  
  result.extend(left[left_index:])
  result.extend(right[right_index:])
  
  return result

def test_function(test_case):
  output = rearrange_digits(test_case[0])
  solution = test_case[1]
  if sum(output) == sum(solution):
    print("Pass")
  else:
    print("Fail")


# Test Case 1: Sanity test
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

# Test Case 2: Empty array
test_case = [[], [0, 0]]
test_function(test_case)
# should pass test case with [0, 0] as the result

# Test Case 3: Abnormal array elements
test_function([[1, 2, -6, 4, 5], [0, 0]])
test_function([[1, 3, 'test', 5, 9], [0, 0]])
# should pass test case with [0, 0] as the result