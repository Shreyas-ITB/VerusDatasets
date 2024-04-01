import re

input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r", encoding='utf-8') as f:
    lines = f.readlines()
    new_lines = []
    for line in lines:
        # Remove all digits from the line
        line = re.sub(r'\d+', '', line)
        # Replace double quotes with single quotes
        line = line.replace('"', "'")
        # Remove unwanted spaces and newlines
        line = ' '.join(line.split())
        if line.strip():
            new_lines.append(line + "\n")

with open(output_file, "w", encoding='utf-8') as f:
    f.writelines(new_lines)

print("Conversion complete!")
