name = input("Please enter your name: ")
filename = open("name.txt", "w")
print(f"{name}", file=filename)
filename.close()

filename = open("name.txt", "r")
for line in filename:
    print(line, end="")
filename.close()

infile = open("numbers.txt", "r")
number1 = int(infile.readline())
number2 = int(infile.readline())
sum_total = number1 + number2
print(number1, number2)
print(sum_total)
infile.close()

with open("numbers.txt", "r") as file:
    for line in file:
        final_total = sum_total + int(line)
print(final_total)