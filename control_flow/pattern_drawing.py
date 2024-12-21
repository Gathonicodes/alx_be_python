# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Use a while loop to iterate through each row of the pattern
row = 0
while row < size:
    # Use a for loop to print asterisks for each column in the row
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after each row
    row += 1  # Increment the row counter
