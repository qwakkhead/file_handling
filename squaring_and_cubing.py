# Read integers from integers.txt
with open("integers.txt", "r") as file:
    numbers = [int(num) for num in file.read().split()]

# Calculate the squares of even integers and cubes of odd integers
even_numbers_squared = [num ** 2 for num in numbers if num % 2 == 0]
odd_numbers_cubed = [num ** 3 for num in numbers if num % 2 != 0]

# Write squares of even integers to double.txt (New file for squared even integers)
with open("double.txt", "w") as even_file:
    for num in even_numbers_squared:
        even_file.write(str(num) + "\n")

# Write cubes of odd integers to triple.txt (New file for cubed odd integers)
with open("triple.txt", "w") as odd_file:
    for num in odd_numbers_cubed:
        odd_file.write(str(num) + "\n")