#1
#12
#123
#1234
#12345
rows = int(input('Enter a number of rows : '))
for row in range(1, rows + 1):
    for col in range(1, rows + 1):
        if col <= row:
            print(col, end=" ")
    print()