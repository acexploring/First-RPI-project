def generate_matrix(array1, array2, n):
    """
    Generates a matrix where:
    - The first row is array1
    - The second row is array2
    - Each subsequent column is the sum of the two previous columns.

    :param array1: List of integers (first row of the matrix)
    :param array2: List of integers (second row of the matrix)
    :param n: Number of columns in the matrix
    :return: Generated matrix
    """
    if len(array1) != len(array2):
        raise ValueError("array1 and array2 must have the same length")
    if len(array1) < 2:
        raise ValueError("array1 and array2 must have at least 2 elements")

    # Initialize the matrix with the first two rows
    matrix = [array1[:], array2[:]]

    # Generate the remaining columns
    for i in range(len(array1), n):
        new_value_row1 = matrix[0][i - 1] + matrix[0][i - 2]
        new_value_row2 = matrix[1][i - 1] + matrix[1][i - 2]
        matrix[0].append(new_value_row1)
        matrix[1].append(new_value_row2)

    return matrix


# Example usage
array1 = [3, 2, 1]
array2 = [4, 5, 6]
n = 6
result = generate_matrix(array1, array2, n)
for row in result:
    print(row)