def searchMatrix(matrix, target):
    curr = 0

    for i in range(len(matrix)):
        element = matrix[i][0]
        if element < target:
            curr = i
        elif element == target:
            return True
        else:
            break

    for j in range(len(matrix[curr])):
        if matrix[curr][j] == target:
            return True
    
    return False
