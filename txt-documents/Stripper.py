import re

def process_file(file_path):
    with open(file_path, 'r') as file:
        # Define a regular expression pattern for matching the specified format
        pattern = re.compile(r'^\s*(-+\s*\d+\s+[\w\d-]+\s*-+)\s*$')

        # Flag to indicate whether to print the next line
        print_next_line = False

        for line in file:
            # Print each line for debugging
            print(f"Line: {line.strip()}")

            # If the line matches the pattern, set the flag to True
            if pattern.match(line.strip()):
                print_next_line = True
            elif print_next_line:
                # If the flag is set, print the current line and reset the flag
                print(line.strip())
                print_next_line = False

# Replace 'your_file.txt' with the actual path to your text file
file_path = '1.txt'
process_file(file_path)
