def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """

    # Check if the input is a string
    if not isinstance(s, str):
        print("Input must be a string.")
        return
    
    # Reverse the string
    reversed_string = s[::-1]

    # Return the reversed string
    return reversed_string 

# Task 2
# Invoke the function "string_reverse" using the following scenarios:

# Run Task 2
# - "Hello World"
print("(1) q4_Task 2A:")
print(string_reverse("Hello World")) # Expected output: "dlroW olleH"

# - "Python"
print("(2) q4_Task 2B:s")
print(string_reverse("Python")) # Expected output: "nohtyP"
