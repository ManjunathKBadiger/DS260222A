#12345
#1234
#123
#12
#1
rows = int(input('Enter a number of rows : '))

for row in range(1, rows + 1):
    number = 1
    for col in range(1, rows + 1):
        if col >= row:
            print(number, end=" ")
            number += 1
    print()

