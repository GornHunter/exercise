__author__ = 'nancy'

import random


def quick_sort(arr):
    # print arr
    if len(arr) <= 1:
        return arr
    else:
        p = arr[0]
        return quick_sort([n for n in arr[1:] if n < p]) + [p] + quick_sort([n for n in arr[1:] if n > p])

# maxsub_sum
def max_sum(h):
    current_sum = 0
    max_sum = 0
    for i in h:
        current_sum += i
        if current_sum > max_sum:
            max_sum = current_sum
        elif current_sum < 0:
            current_sum = 0
    return max_sum


if __name__ == '__main__':
    arr = []
    i = 0
    for i in range(10):
        arr.append(random.randint(-50, 100))
    print 'before sort', arr
    h = quick_sort(arr)
    print 'after sort', h
    print 'sum',max_sum(h)

