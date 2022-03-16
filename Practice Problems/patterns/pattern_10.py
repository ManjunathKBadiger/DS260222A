# 5 5 5 5 5 
# 4 4 4 4   
# 3 3 3     
# 2 2       
# 1
rows = int(input('Enter a number of rows : '))

for row in range(1, rows + 1):
    number = rows
    for col in range(1, rows + 1):
        if col >= row:
            print(number, end=" ")
            number -= 1
    print()