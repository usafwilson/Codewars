# The objective is to return all pairs of integers from a given
# array of integers that have a difference of 2.
#
# The result array should be sorted in ascending order of values.
#
# Assume there are no duplicate integers in the array. The order of the
# integers in the input array should not matter.


def twos_difference(lst):
    ret_list = []
    for i in range(len(lst)):
        for n in lst:
            if lst[i] - n == 2 and (n,lst[i]) not in ret_list:
                ret_list.append((n,lst[i]))
            elif n - lst[i] == 2 and (lst[i],n) not in ret_list:
                ret_list.append((lst[i],n))
    return sorted(ret_list)

#     Community Solution
# def twos_difference(a):
#     s = set(a)
#     return sorted((x, x + 2) for x in a if x + 2 in s)