import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def process_numbers():
    # Open file numbers.txt
    filename = filedialog.askopenfilename(title="Select numbers.txt", filetypes=(("Text files", ".txt"), ("All files", ".*")))
    if filename:
        # Read numbers from numbers.txt
        with open(filename, "r") as file:
            numbers = [int(num) for num in file.read().split()]

        # Making even and odd numbers separator 
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

        # done
        messagebox.showinfo("Success", "Files even.txt and odd.txt created successfully.")

# Create tkinter window
root = tk.Tk()
root.title("Number File Processor")

# Create button to trigger file processing
process_button = tk.Button(root, text="Process Numbers", command=process_numbers)
process_button.pack(pady=10)

# Run the tkinter event loop
root.mainloop()