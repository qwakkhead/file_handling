# Make a file for writing
with open("mylife.txt", "w") as file:
    # Continue the loop until the user has no lines to enter
    while True:
        # Prompt the user to enter a line
        line = input("Enter line: ")
        
        # Write the line to the file
        file.write(line + "\n")
        
        # Ask the user if he/she wants to add more lines
        more_lines = input("Are there more lines? (y/n) ").strip().lower()
        
        # If the user indicates no more lines, break the loop
        if more_lines != 'y':
            break

