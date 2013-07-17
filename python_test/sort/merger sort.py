__author__ = 'nancy'

# import sys
# sys.setrecursionlimit(10)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left = []
    right = []
    l = int(len(arr)) / 2
    for num in arr[:l]:
        left.append(num)
    for num in arr[l:]:
        right.append(num)
    left = merge_sort(left)
    right = merge_sort(right)
    print(left, right)
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

def main():
    arr = [6, 5, 3, 1, 8, 7, 2, 4]
    m = merge_sort(arr)
    print(m)


if __name__ == '__main__':
    main()