#54321
#4321
#321
#21
#1
rows = int(input('Enter a number of rows : '))
number = 5
for row in range(1, rows + 1):
    for col in range(1, rows + 1):
        if col >= row:
            print(number, end=" ")
            number -= 1
    number = rows - row
    print()