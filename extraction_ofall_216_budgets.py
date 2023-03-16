import re

# Open the text file and read the contents
with open('result_gap_edp_ep4.txt', 'r') as file:
    text = file.read()

# Define the regular expression pattern
pattern = r'test/acc last (\d+\.\d+) mean (\d+\.\d+)'

# Find all the matches that follow the pattern
matches = re.findall(pattern, text)

# Print the matches
for match in matches:
    print(f"test/acc last {match[0]} mean {match[1]}")
