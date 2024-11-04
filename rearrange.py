"""
In this program, we will list the even numbers before the odd numbers
"""

LIST_NUMBERS = []

EVEN_NUMBERS = []
ODD_NUMBERS = []

def special_rearrangement(nums):
# In this for loop, we will check if the number is even or odd
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print(nums)
    for sort in sorted(nums):
        if sort % 2 == 0:
            print(sort, " is an even number")
            EVEN_NUMBERS.append(sort)
        else:
            print(sort, " is an odd number")
            ODD_NUMBERS.append(sort)

special_rearrangement(LIST_NUMBERS)
# Then  we will add the numbers sorted from even to odd numbers in the list
NUMBERS_COMBINED = EVEN_NUMBERS + ODD_NUMBERS
print("This is the list with an even numbers before odd numbers:", NUMBERS_COMBINED)