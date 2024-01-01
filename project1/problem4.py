class Group(object):
  def __init__(self, _name):
    self.name = _name
    self.groups = []
    self.users = []

  def add_group(self, group):
    self.groups.append(group)

  def add_user(self, user):
    self.users.append(user)

  def get_groups(self):
    return self.groups

  def get_users(self):
    return self.users

  def get_name(self):
    return self.name


def is_user_in_group(user, group: Group):
  """
  Return True if user is in the group, False otherwise.

  Args:
    user(str): user name/id
    group(class:Group): group to check user membership against
  """
  if group:
    if user in group.get_users(): return True

    for sub_group in group.get_groups():
      return is_user_in_group(user, sub_group)

  return False

# Test Case 1: Implemented function works as expected
print('\n--- Test Case 1 ---')
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group(sub_child_user, parent))
# return True as sub_child_user is in the parent group
print(is_user_in_group('test_user', child))
# return False as user is not in the child group

# Test Case 2: Other test groups and users
print('\n--- Test Case 2 ---')
project = Group('project')
developers = Group('developers')
seniors = Group('seniors')
juniors = Group('juniors')
developers.add_group(seniors)
developers.add_group(juniors)
project.add_group(developers)
junior_devs = ['Hoag', 'Vinh', 'Thy']
for junior in junior_devs: juniors.add_user(junior)
senior_devs = ['Dat', 'Binh', 'Tuan']
for senior in senior_devs: seniors.add_user(senior)
project.add_user('PM')
print(is_user_in_group('PM', developers))
print(is_user_in_group('PM', project))
# return False, True as PM is in project group and not in developers group
print(is_user_in_group('Hoag', juniors))
print(is_user_in_group('Hoag', seniors))
# return True, False as Hoag is in juniors group only

# Test Case 3: Invalid group
print('\n--- Test Case 3 ---')
print(is_user_in_group('test_user', ''))
print(is_user_in_group('test_user', None))
# return False as the group is invalid
