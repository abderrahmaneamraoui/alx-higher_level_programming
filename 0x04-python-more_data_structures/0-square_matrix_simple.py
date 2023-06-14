#!/urs/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    new_matrix = [[0 for col in range(len(matrix[row]))] for row in range(len(matrix))]
    
    # Calculate the square of each element in the input matrix and store it in the new matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] ** 2
    
    return new_matrix
