def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """

    # Check if num and divisor are numeric
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return "Both num and divisor must be numeric"
    
    # Check if divisor is not zero
    if divisor == 0:
        return "Divisor cannot be zero"
    
    # Check if num is divisible by divisor
    if num % divisor == 0:
        return True
    else:
        return False


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:

# Run Task 2 using the following scenarios
# - 10, 2
print("(1) q5_Task 2A:")
print(check_divisibility(10, 2))  # - True

# Run Task 2 using the following scenarios
# - 7, 3
print("(2) q5_Task 2B:")
print(check_divisibility(7, 3))  # - False
