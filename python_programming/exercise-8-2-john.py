def get_cell_value(x,y):
    return x*y

def print_cell(value):
    print("{0:8}".format(value), end="")

row_list = list(range(0, 55, 5))
column_list = list(range(-20, 70, 10))
print("{0:>8}".format("r/c"), end="")
for header in column_list:
    print_cell(header)
print()

for row in row_list:
    print_cell(row)
    for column in column_list:
        print_cell(get_cell_value(row, column))
    print("")