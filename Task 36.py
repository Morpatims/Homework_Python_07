def print_operation_table(operation, num_rows=6, num_columns=6):
    table = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    max_length = len(str(max(max(table))))
    for row in table:
        row_str = ' '.join([f"{x:>{max_length}}" for x in row])
        print(row_str)

print_operation_table(lambda x, y: x * y)