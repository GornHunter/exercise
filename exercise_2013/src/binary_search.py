__author__ = 'Nancy'

# %%%%%%%%%%%%the first%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# def binary_search(array, begin, end, key):
#     print("begin=%d, end=%d, key=%d" % (begin, end, key))
#     if begin > end:
#         return -1
#     mid = int((begin + end) / 2)
#     if key == array[mid]:
#         return mid
#     elif key < array[mid]:
#         return binary_search(array, begin, mid - 1, key)
#     else:
#         return binary_search(array, mid + 1, end, key)
#
#
# print(binary_search([1, 2, 3, 4, 5, 6, 7], 0, 6, 4))
# print(binary_search([1, 2, 3, 4, 5, 6, 7], 0, 6, 54))

# %%%%%%%%%%%%the second%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def binary_search2(array, key):
    min, max = 0, len(array) - 1
    mid = int((min + max) / 2)
    while min < max:
        if array[mid] < key:
            min = mid + 1
        elif array[mid] > key:
            max = mid - 1
        else:
            return mid
    return -1


# print(binary_search([1, 2, 3, 4, 5, 6, 7], 0, 6, 4))

# %%%%%%%%%%%%the third%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def binary_search(array, key):
    min, max = 0, len(array) - 1
    while min < max:
        mid = int((min + max) / 2)
        if array[mid] < key:
            min = mid + 1
        else:
            max = mid
    if min == max and array[min] == key:
        return min
    else:
        return -1

# print(binary_search([1, 2, 3, 4, 5, 6, 7], 0, 6, 4))



