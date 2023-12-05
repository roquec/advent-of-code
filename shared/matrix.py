def array_get(array, index, default):
    if index < 0 or index >= len(array):
        return default
    else:
        return array[index]


def array_range(array, start, end, default):
    a = [default] * (0 - start)
    b = array[max(start, 0):end]
    c = [default] * (end - len(array))
    return ''.join(a) + b + ''.join(c)


def matrix_get(matrix, col_index, row_index, default):
    width = len(matrix[0])
    col = array_get(matrix, col_index, [default] * width)
    result = array_get(col, row_index, default)
    return result


def matrix_range(matrix, col_index, row_start, row_end, default):
    if col_index < 0 or col_index >= len(matrix):
        return [default] * (row_end - row_start)
    else:
        return array_range(matrix[col_index], row_start, row_end, default)
