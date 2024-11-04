"""
In this program, we will list the even numbers before the odd numbers
"""

LIST_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(LIST_NUMBERS)

EVEN_NUMBERS = []
ODD_NUMBERS = []

for sort in sorted(LIST_NUMBERS):
    if sort % 2 == 0:
        EVEN_NUMBERS.append(sort)
        print(sort, " is an even number")
    else:
        ODD_NUMBERS.append(sort)
        print(sort, " is an odd number")

NUMBERS_COMBINED = EVEN_NUMBERS + ODD_NUMBERS
print("This is the list with an even numbers before odd numbers:", NUMBERS_COMBINED)