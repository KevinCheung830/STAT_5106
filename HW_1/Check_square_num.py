import math

def is_perfect_square(n):
    """
    Check if a number is a perfect square using math.isqrt()
    
    Parameters:
    n (int): Number to check
    
    Returns:
    bool: True if perfect square, False otherwise
    """
    if n < 0:
        return False
    if n == 0:
        return True
    
    root = math.isqrt(n)  # Integer square root
    return root * root == n

# Test examples
test_numbers = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 200, 300, -4]
for num in test_numbers:
    print(f"{num}: {is_perfect_square(num)}")