# This file will be used to remove comments and definitions
# from any given file and copy the result to the clipboard
# to ensure the code submitted to leetcode is removed of artificial runtime increase

import pyperclip

# Define the input file path
num = input('What file number should be cleaned and copied?\n')
input_file_path = f"solutions/{num}.py"

output = ""

# Open the input file in read mode
with open(input_file_path, 'r') as input_file:
    # Flag to indicate if we should start copying lines
    copying = False

    # Iterate through each line in the input file
    for line in input_file:
        # Check if the line contains "class Solution:"
        if "class Solution:" in line:
            copying = True
        # If copying has begun and line is not a comment or whitespace,
        if copying and not line.strip().startswith("#") and len(line.strip()) != 0:
            # Write the line to the output string
            output += line

# Print a message to indicate the process is complete
pyperclip.copy(output)
print("Output copied to clipboard")
