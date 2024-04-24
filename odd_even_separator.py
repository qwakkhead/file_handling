# Read numbers from numbers.txt
with open("numbers.txt", "r") as file:
    numbers = [int(num) for num in file.read().split()]

# Make an even and odd numbers function
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Write even numbers to even.txt (new file for even numbers)
with open("even.txt", "w") as even_file:
    for num in even_numbers:
        even_file.write(str(num) + "\n")

# Write odd numbers to odd.txt (new file for odd numbers)
with open("odd.txt", "w") as odd_file:
    for num in odd_numbers:
        odd_file.write(str(num) + "\n")