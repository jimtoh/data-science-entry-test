def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """

    # Create a new list to store the modified list
    new_lst = []

    # Iterate through the list
    for val in lst:
        # If the value is equal to find_val, replace it with replace_val
        if val == find_val:
            new_lst.append(replace_val)
        else:
            new_lst.append(val)
    
    # Return the modified list
    return new_lst


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:

# Run Task 2
# - [1, 2, 3, 4, 2, 2], 2, 5
print("(1) q2_Task 2A:")
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)) # Result: [1, 5, 3, 4, 5, 5]

# Run Task 2
# - ["apple", "banana", "apple"], "apple", "orange"
print("(2) q2_Task 2B:")
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange")) # Result: ["orange", "banana", "orange"]