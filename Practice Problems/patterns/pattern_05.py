#1
#22
#333
#4444
#55555
rows = int(input('Enter a number of rows : '))
for row in range(1, rows + 1):
    for col in range(1, rows + 1):
        if col <= row:
            print(row, end=" ")
    print()