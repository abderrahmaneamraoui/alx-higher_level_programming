def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Print the element with a width of 2 and a right alignment
            print("{:d}".format(row[i]).rjust(2), end="")
            # Print a space after each element, except for the last one in the row
            if i != len(row) - 1:
                print(" ", end="")
        # Print a newline after each row
        print()
