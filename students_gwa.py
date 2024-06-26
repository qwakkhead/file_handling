from fancify_text import blue
from fancify_text import script

# Read student names and GWAs from file
with open("student_gwa.txt", "r") as file:
    lines = file.readlines()

students_gwas = [line.strip().split() for line in lines]

# Initialize highest and lowest GWAs
highest_gwa = 0.00
lowest_gwa = 5.00
highest_student = None
lowest_student = None

for student, gwa in students_gwas:
    gwa = float(gwa)
    if gwa > highest_gwa: 
        highest_gwa = gwa
        highest_student = (student, gwa)
    if gwa < lowest_gwa:
        lowest_gwa = gwa
        lowest_student = (student, gwa)

# Output the student with the highest GWA
if highest_student:
    print(script("Student with the lowest GWA:"))
    print(blue(f"Name: {highest_student[0]}"))
    print(blue(f"GWA: {highest_student[1]}"))
else:
    print("No student found with the lowest GWA.")

# Output the student with the lowest GWA
if lowest_student:
    print(script("\nStudent with the highest GWA:"))
    print(blue(f"Name: {lowest_student[0]}"))
    print(blue(f"GWA: {lowest_student[1]}"))
else:
    print("No student found with the highest GWA.")
