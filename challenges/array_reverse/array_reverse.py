arr = [1,2,3,4,5,6,7]
new_arr = []
i = len(arr) - 1

def reverseArray():
  while i >= 0:
    new_arr.append(arr[i])
    i-=1
print(new_arr)