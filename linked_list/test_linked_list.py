from linked_list import linked_list

def test_one():
  my_list = linked_list()
  my_list.insert(4)
  expected = True
  actual = my_list.includes(4)
  assert actual == expected

def test_two():
  my_list = linked_list()
  my_list.insert(4)
  expected = False
  actual = my_list.includes(5)
  assert actual == expected

############################################################

# def test_three():
#   my_list = to_list()
#   my_list.insert(5)
#   expected = True
#   actual = my_list.includes(4)
#   assert actual == expected

# def test_four():
#   my_list = to_list()
#   my_list.insert(4)
#   expected = False
#   actual = my_list.includes(5)
#   assert actual == expected