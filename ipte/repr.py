# Define the list of parts
parts = ['part1', 'part2', 'part3']

# Function to process each part
def process_part(part):
    # Imagine this function performs some complex operations
    return f"processed_{part}"

# Process all parts using a list comprehension for efficiency
processed_parts = [process_part(part) for part in parts]

# Output the processed parts
print(processed_parts)
