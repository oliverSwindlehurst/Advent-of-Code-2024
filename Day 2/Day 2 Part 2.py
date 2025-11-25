# Function to determine if a given row is "safe"
def is_safe(row):
    # Calculate the difference between consecutive elements in the row
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    
    # Check if all the differences are in the range {1, 2, 3} or {-1, -2, -3}
    # `set(inc)` ensures unique differences and `<=` checks if the set is a subset
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True  # The row is safe
    return False  # The row is not safe

# Read input data from the file and parse it into a list of lists of integers
# Each line in the file is split into integers and added to the `data` list
data = [[int(y) for y in x.split(' ')] for x in open('Day 2\Input.txt').read().split('\n')]

# Modified safe row calculation:
# For each row, consider removing one element at a time and check if the remaining
# elements form a "safe" row. Count how many rows have at least one such removal
safe_count = sum([
    # Check if the row becomes safe after removing any single element
    any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) 
    for row in data
])
print(safe_count)  # Print the modified safe row count
