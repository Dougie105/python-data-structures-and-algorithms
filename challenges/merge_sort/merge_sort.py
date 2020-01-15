def split(lst):
    """ Splits a lst into two pieces """
    length = len(lst)
    center = length // 2
    return lst[:center], lst[center:]

def merge_sorted_lists(L, R):
    """ Merge two sorted lists """
    if len(L) == 0:
        return R
    elif len(R) == 0:
        return L

    L_idx = R_idx = 0
    merged_list = []
    list_len_target = len(L) + len(R)

    while len(merged_list) < list_len_target:
        if L[L_idx] <= R[R_idx]:
            merged_list.append(L[L_idx])
            L_idx += 1
        else:
            merged_list.append(R[R_idx])
            R_idx += 1

        if R_idx == len(R):
            merged_list += L[L_idx:]
            break

        elif L_idx == len(L):
            merged_list += R[R_idx:]
            break

    return merged_list

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        left, right = split(lst)
        return merge_sorted_lists(merge_sort(left), merge_sort(right))