# Selection Sort Method

## Whiteboard
![selection_sort](assets/select_sort.png)

## Code

def selection_sort(array):
    x = len(array)

    for i in range(x):

        lowest_value = i

        for j in range(i + 1, x):
            if array[j] < array[lowest_value]:
                lowest_value = j

        array[lowest_value], array[i] = array[i], array[lowest_value]


## Tests

expected = [4,8,15,16,23,42]
array = [8,4,23,42,16,15]
selection_sort(array)

assert array == expected


## Walkthrough

##### You would start at 8 and by definition that is the lowest number.
##### Then you would compare 4 with 8.
##### 4 is smaller than 8 so 4 gets placed under the lowest_value variable.
##### Then you compare 23 and 8 and so on until you compare the 15 and 8.
##### With 4 still the lowest number at the end of one pass through, the lowest_value and the value at i swap.
##### The new array is now [4, 8, 23, 42, 16, 15]
##### The second pass though starts by comparing the 8 to everything else in the array, since 8 is lower than everything after it, 8 stays in its place and the second pass through is over.
##### The array is still [4, 8, 23, 42, 16, 15]
##### The third pass through the pointer starts at 23, and compare wiht the 42. lowest_value = 23
##### Then you compare the 23 with the 16. lowest_value = 16
##### Then you compare the 23 with the 15. lowest_value = 15
##### Since i was in the position of 42, 42 and 15 will swap locations.
##### The new array is now [4, 8, 15, 42, 16, 23]
##### Now you compare the the 15 with the 42. lowest_value = 15
##### Then 15 and 16. Then 15 and 23. Since 15 is the lowest it stays put.
##### The array is still [4, 8, 15, 42, 16, 23]
##### Pointer then starts at 42 and compars to 16. lowest_value = 16
##### Compars the 42 with the 23. With the lowest value being 16 at the end, 42 and 16 will swap locations.
##### Your new array is [4, 8, 15, 16, 42, 23]
##### Your pointer now stands on 42 and compars itself to the 23. Since 23 is lowest_value.
##### New array = [4, 8, 15, 16, 23, 42]
##### Your array is now sorted and is done running.

# Merge Sort

## Whiteboard
![merge_sort](assets/merge_sort.png)

## Code

def merge_sort(array):
        merge_sort2(array, 0, len(array)-1)

def merge_sort2(array, first, last):
        if first < last:


## Tests

expected = [4,8,15,16,23,42]
array = [8,4,23,42,16,15]
merge_sort(array)

assert array == expected


## Walkthrough

                [5,1,3,2,4] # Input
                /      \
                [5,1,3]  [2,4] # Split the list into sub lists based on the mid
                /   \    \  \
                [5,1] [3]  [2] [4]
                / \     \    \   \
                [5] [1]  [3]  [2] [4] # Separate the list to the smallest parts
                \   /   /    /   /
                [1,5]  [3]  [2] [4] # Sort the value as you merge the lists back together
                |   /    /  /
                [1,3,5]   [2,4]
                \     /
                [1,2,3,4,5] # Output