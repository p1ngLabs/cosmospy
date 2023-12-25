import os

def find_files(suffix: str, path: str):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    isPathValid = os.path.exists(path)
    if not isPathValid:
      print("Invalid path")
      return []
    
    suffix = suffix.strip('.')
    result = set()
    current_list = os.listdir(path)

    for current in current_list:
      # format pathname to include current directory
      pathname = f"{path}/{current}"
      is_dir = os.path.isdir(pathname)
      is_file = os.path.isfile(pathname)

      # if current is a directory, call `find_files` recursively
      if is_dir: result = result.union(find_files(suffix, pathname))
      
      # if current is a file and has the given suffix, add to returned list of paths
      if is_file:
        current_suffix = current.split('.')[1]
        if current_suffix == suffix:
          result.add(pathname)
   
    return result

def print_result(result):
  for path in result:
    print(path)

# Test Case 1: Work as expected with give `testdir`
print('\n--- Test Case 1 ---')
result = find_files('.c', './testdir')
print_result(result)

# Test Case 2: Empty directory
print('\n--- Test Case 2 ---')
result = find_files('.c', './testempty')
print_result(result)
# Nothing is printed since there are no .c files

# Test Case 3: Invalid pathname
print('\n--- Test Case 3 ---')
result = find_files('.c', './no_exists')
print_result(result)
# Print 'Invalid path'