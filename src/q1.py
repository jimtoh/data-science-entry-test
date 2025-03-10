def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1

    # Swapping values
    x = x + y
    y = x - y
    x = x - y

    print(x, y)
    return

# Task 1
# Invoke the function "swap" using the following scenarios:
# - 10, 20
print("Task 1")
print(swap(10, 20)) # Expected output: 20 10

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
print()
print("Task 2")
print(swap("Apple", 10)) # Expected output: -1
print(swap(9, 17)) # Expected output: 17 9

# Run the code
# python src/q1.py