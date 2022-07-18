
"""Question 3"""

import NumPy

array = ([3, 6, 8, 10, 12])

def numbers(array):
    for x in array:
        print(x**2)
    return

numbers(array)

"""Question 4"""

"""Question 9"""

numbers = [3, 5, -4, 40, 11, 1, -1, 60]
target_number = 100

for i, number in enumerate(numbers[:-1]):
    complementary = target_number - number
    if complementary in numbers[i + 1:]:
        print(number, complementary)
        break
else:
    print([])

