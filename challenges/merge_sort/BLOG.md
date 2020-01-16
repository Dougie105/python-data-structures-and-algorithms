# Merge Sort

## Whiteboard
![merge_sort](assets/merge_sort.png)

## Code

```python
def merge_sort(array):
        merge_sort2(array, 0, len(array)-1)

def merge_sort2(array, first, last):
        if first < last:
```

## Tests

expected = [4,8,15,16,23,42]
array = [8,4,23,42,16,15]
merge_sort(array)

assert array == expected


## Walkthrough

##### You are going to be starting out with one list and pass that list into the merge_sort function.
#####You are going to go ahead and say that if the length of the list is less than or equil to one then return the list.
##### else you are going to set the variable lft and right equil to the split of the list.
##### Create a seperate split function that takes in a list and finds the length, center, and then splits the list into 2 lists (L and R).
##### After it is split and you return 2 lists, you need to pass those into a merge sorted list function.
##### That function is going to look at list L and if it equils 0 then it will return R and vice versa.
##### Set the index of both L and R to zero
##### set a new variable for the completed merged list to go to an empty list.
##### Go ahead and set the definate length of the new list by setting a target lenght to L + R
##### While the lenght of the empty list is less than the target length you are going to want to do a few things.
##### * if L is less than or equil to R you want to append the value of L as well as increase the L index by one.
##### else append the R.
##### If the R index is equal to the length of R you are goiing to break. Do the same with L.
##### return the final list.