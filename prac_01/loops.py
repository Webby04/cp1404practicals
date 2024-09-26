for i in range(1, 21, 1):
    print(i, end=' ')
print()

# Part A
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Part B
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Part C
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end='')
print()

# Part D
number_of_stars = int(input("Number of stars: "))
for i in range(1, number_of_stars + 1):
    print("*" * i)
print()