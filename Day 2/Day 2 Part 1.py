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

# Count the number of "safe" rows using the `is_safe` function
safe_count = sum([is_safe(row) for row in data])
print(safe_count)  # Print the count of safe rows
