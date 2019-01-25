example = [["Name", "Age"], ["Nate", "23"], ["Dillon", "22"], ["Bob", "0"]]

def column_widths(data):
    widths = {}
    for h in range (0, len(data[0])):
        max_length = 0
        for row in data:
            if len(row[h]) > max_length:
                max_length = len(row[h])
        widths[h] = max_length 
    return widths

w = column_widths(example)
# print(w[0])

# | item | item | item |
def print_table_row(data, column_widths, is_underlined = False):
    row = ""
    for i in range(0, len(data)):
        diff = abs(column_widths[i] - len(data[i]))
        row = row + "| "
        row =  row + data[i] + (" " * diff)
        row = row + " "
    row = row + "|"
    print(row)
    if is_underlined:
        print("-" * len(row))

def print_table(data):
    widths = column_widths(data)
    print_table_row(data[0], widths, True)
    for row in data[1:]:
        print_table_row(row, widths)

# print_table(example)

