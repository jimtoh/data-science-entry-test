def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    # Return "No negatives" if the list is empty
    if len(lst) == 0:
        return "No negatives"
    # Initialize the index to 0
    index = 0

    # Loop through the list
    while index < len(lst):
        # Check if the current element is negative
        if lst[index] < 0:
            return lst[index]
        # Increment the index
        index += 1
    # Return "No negatives" if no negative number is found
    return "No negatives"


# Task 2
# Invoke the function "find_first_negative" using the following scenario:

# Run Task 2 using the following scenarios
# - [3, 5, -1, 7, -2, 8]
print("(1) q6_Task 2A:")
print(find_first_negative([3, 5, -1, 7, -2, 8]))  # -1

# Run Task 2 using the following scenarios
# - [2, 10, 7, 0]
print("(2) q6_Task 2B:")
print(find_first_negative([2, 10, 7, 0]))  # No negatives
