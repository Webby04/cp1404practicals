numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

first_number = numbers[0]
last_number = numbers[-1]
smallest_number = min(numbers)
largest_number = max(numbers)
average_number = sum(numbers) / len(numbers)

print(f"The first number is {first_number}")
print(f"The last number is {last_number}")
print(f"The smallest number is {smallest_number}")
print(f"The largest number is {largest_number}")
print(f"The average of the numbers is {average_number}")

