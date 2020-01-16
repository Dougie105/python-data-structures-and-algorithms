def selection_sort(array):
    x = len(array)

    for i in range(x):

        lowest_value = i

        for j in range(i + 1, x):
            if array[j] < array[lowest_value]:
                lowest_value = j

        array[lowest_value], array[i] = array[i], array[lowest_value]
    return array

print(selection_sort([8,7,6,5,4,3,2,1,9]))