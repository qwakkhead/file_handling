# Open the mylife.txt for writing
with open("mylife.txt", "w") as file:
 
    while True:
        # Asks the user to enter a line
        line = input("Enter line: ")
        
        # Write the line to the file
        file.write(line + "\n")
        
        # Ask the users if there are more lines to be entered
        more_lines = input("Are there more lines? (y/n) ").strip().lower()
        
        # If no more lines, break the loop
        if more_lines != 'y':
            break

