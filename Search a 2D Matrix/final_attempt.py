def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    low = 0
    high = (m * n) - 1

    while low <= high:
        mid = (low + high) // 2
        row_index = mid // n
        col_index = mid % n
        curr = matrix[row_index][col_index]

        if curr < target:
            low = mid + 1
        elif curr > target:
            high = mid - 1
        else:
            return True

    return False
