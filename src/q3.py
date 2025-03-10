def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """

    # Check if the key exists in the dictionary
    if key in dct:
        # Print the original value of the key
        print("Original value:", dct[key])

        # Update the value of the key
        dct[key] = value
    else:
        # Add the key-value pair to the dictionary
        dct[key] = value
    return dct

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:

# Run Task 2 with the following scenarios
# - {}, "name", "Alice"
print("(1) q3_Task 2A:")
print(update_dictionary({}, "name", "Alice")) # Original

# Run Task 2 with the following scenarios
# - {"age": 25}, "age", 26
print("(2) q3_Task 2B:")
print(update_dictionary({"age": 25}, "age", 26)) # Original value: 25