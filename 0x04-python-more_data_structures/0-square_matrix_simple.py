#!/urs/bin/python3
def square_matrix_simple(matrix=[]):
    return [[y ** 2 for y in x] for x in matrix]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)

print("Original matrix:")
for row in matrix:
    print(row)

print("Squared matrix:")
for row in new_matrix:
    print(row)
