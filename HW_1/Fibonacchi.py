import math

def is_fibonacci(x):
    """
    Check if a number is Fibonacci using mathematical property
    
    Parameters:
    x (int): Number to check
    
    Returns:
    bool: True if Fibonacci, False otherwise
    """
    if x < 0 :
        return False
    #Edge case for 0,1,2,3 since they are Fibonacci numbers but smaller than 4
    elif x == 0 or x == 1 or x == 2 or x == 3:
        return True
    # Check: 5*x² + 4 OR 5*x² - 4 is a perfect square
    condition1 = 5 * x * x + 4
    condition2 = 5 * x * x - 4
    
    root1 = math.isqrt(condition1)
    root2 = math.isqrt(condition2)
    
    return (root1 * root1 == condition1) or (root2 * root2 == condition2)

# Test
fib_numbers = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
non_fib_numbers = [4, 6, 7, 9, 10, 11, 12, 14, 15, 100]

print("Fibonacci numbers:")
for num in fib_numbers:
    print(f"{num}: {is_fibonacci(num)}")

print("\nNon-Fibonacci numbers:")
for num in non_fib_numbers:
    print(f"{num}: {is_fibonacci(num)}")