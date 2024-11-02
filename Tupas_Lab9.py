row = int(input("Enter the number of rows: "))
number = 1
for a in range(1, row + 1):
    for b in range(a):
        print(number, end=' ')
        number += 1
    print()