def ceil(x):
    return -int(-x // 1)


def printrow(rows, cols, row_type):
    if rows == 0 and cols == 1:
        print("  ___")
        print(" /   \\")
        print(" \\___/")
    elif rows == 0 and cols > 1:
        if row_type == 'top':
            if cols % 2 == 0:
                print("  ___" + "     ___" * ((cols // 2) - 1))
                print(" /   \\" + "___/   \\" * ((cols // 2) - 1) + "___")
            else:
                print("  ___" + "     ___" * (ceil(cols // 2)))
                print(" /   \\" + "___/   \\" * ((cols // 2)))

        elif row_type == 'bottom':
            if cols % 2 == 0:
                print(" \\___/" + "   \\___/" * ((cols // 2) - 1))
                print("     \\___/" + "   \\___/" * ((cols // 2) - 1))
            else:
                print(" \\___/" + "   \\___/" * (ceil(cols // 2)))
                print("     \\___/" + "   \\___/" * ((cols // 2) - 1))

    else:

        if row_type == 'top':
            if cols % 2 == 0:
                print("  ___" + "     ___" * ((cols // 2) - 1))
                print(" /   \\" + "___/   \\" * ((cols // 2) - 1) + "___")
            else:
                print("  ___" + "     ___" * (ceil(cols // 2)))
                print(" /   \\" + "___/   \\" * ((cols // 2)))
        elif row_type == 'middle':
            if cols % 2 == 0:
                print(" \\___/" + "   \\___/" * ((cols // 2) - 1) + "   \\")
                print(" /   \\" + "___/   \\" * ((cols // 2) - 1) + "___/")
            else:
                print(" \\___/" + "   \\___/" * (cols // 2))
                print(" /   \\" + "___/   \\" * (cols // 2))
        elif row_type == 'bottom':
            if cols % 2 == 0:
                print(" \\___/" + "   \\___/" * ((cols // 2) - 1))
            else:
                print(" \\___/" + "   \\___/" * (ceil(cols // 2)))


def printgrid(rows, col):
    if row == 0 and col > 1:
        printrow(rows, col, 'top')
        printrow(rows, col, 'bottom')
    else:
        for r in range(rows + 1):
            if r == 0:
                printrow(rows, col, 'top')
            elif r <= row - 1:
                printrow(rows, col, 'middle')
            else:
                printrow(rows, col, 'bottom')


row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
if row == 1:
    row = 0

printgrid(row, col)
