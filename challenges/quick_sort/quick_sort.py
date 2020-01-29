def quick_sort(lst):

        '''grab the length of the list'''
        length = len(lst)

        '''if the list is empty or equal to one just return the list'''
        if len(lst) <=1:
                return lst

        else:
                '''pop the last element off the list and make that your pivot'''
                pivot = lst.pop()

        '''set two empty lists'''
        items_greater = []
        items_lower = []

        '''if the pointer is larger than the pivot then you are going to put the pointer value in the items_greater list, if it were less than then the value would go into the items_lower list'''
        for pointer in lst:
                if pointer > pivot:
                        items_greater.append(pointer)
                else:
                        items_lower.append(pointer)

        '''this will keep running until there are no values left to compare and return all the values in sorted order'''
        return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


'''fun quick test so you dont have to run pytest'''
print(quick_sort([32,675,87,985,6534,43,54,65,8,8,542,2,6,87,1,5,9,]))