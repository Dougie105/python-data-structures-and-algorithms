def insert_shift_array(lst, val):
  '''A function that takes in an array and the value to be added. Returns an array with the new value added at the middle index.'''
  middle = len(lst) // 2
  if len(lst) % 2 != 0:
    middle += 1
  lst[middle:middle] = [val]
  return lst