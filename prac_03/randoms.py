import random
# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
print(random.randint(5, 20))  # line 1
# The smallest and largest number for line 1 is 5 and 20

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
print(random.randrange(3, 10, 2))  # line 2
# No line 2 won't print 4 because it prints odd numbers from 3 to 10

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
print(random.uniform(2.5, 5.5))  # line 3
# The smallest number it prints is 2.5 and the largest is 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(f"{random.uniform(1, 100):.0f}")