__author__ = 'nancy'

from itertools import permutations




def find_column(arr, n_row, n, is_traceback=False):
    start = 0
    if is_traceback:
        start = arr[n_row] + 1
    for candidate in range(start, n):
        ok = True
        # test to see if is ok
        for i in range(n_row):
            # columns
            if candidate == arr[i]:
                ok = False
                break
            else:
                x1, y1 = arr[i], i
                x2, y2 = candidate,n_row

                if abs(x1- x2) == abs(y1- y2):
                    ok = False
                    break
        if ok==True:
            return candidate
    # can not find one, should trace back
    return None

print(find_column([0, 2, 4, 6, 1,0,0], 4, 8, True) == 3)


def solve_problem(k):
    arr = [0] * k
    row = 0
    while row < k:
        position = find_column(arr, row, k, is_traceback=False)
        if position is not None:
            arr[row] = position
            print('----', arr[:row+1])
        # traceback
        else:
            while True:
                row -= 1
                position = find_column(arr, row,k, is_traceback=True)
                if position is not None:
                    arr[row] = position
                    print(arr[:row+1])
                    break
                elif row == 0:
                    return
        row += 1


if __name__ == "__main__":
    solve_problem(8)
