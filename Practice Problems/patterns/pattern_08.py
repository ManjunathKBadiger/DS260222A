# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5
rows = int(input('Enter a number of rows : '))
for row in range(1, rows + 1):
    for col in range(1, rows + 1):
        if col >= row:
            print(row, end=" ")
    print()