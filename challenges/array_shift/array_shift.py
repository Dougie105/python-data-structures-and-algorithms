def insert_shift_array(lst, val):
  middle = len(lst) // 2
  if len(lst) % 2 != 0:
    middle += 1
  lst[middle:middle] = [val]
  return lst