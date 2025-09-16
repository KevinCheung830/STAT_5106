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

def is_square(n):
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

def is_triangular(x):
    # Given X is the number to check
    # Check if 8*x + 1 is a perfect square and if the square root is odd
    # If so , then it is a triangular number
    if x < 0: return False
    root = math.isqrt(8*x + 1)
    return root*root == 8*x + 1 and root % 2 == 1

def check_mathematical_series(n: int) -> str:
    try:
        n_int = int(n)
    except (ValueError, TypeError):
        return "None"
    
    series = []
    if is_fibonacci(n_int):
        series.append("Fibonacci")
    if is_square(n_int):
        series.append("Square")
    if is_triangular(n_int):
        series.append("Triangular")
    
    if not series:
        return "None"
    else:
        return ", ".join(series)

# Unit tests
def test_check_mathematical_series():
    # Test case 1: n = 0 (Edge case for Fibonacci, Square, Triangular)
    assert check_mathematical_series(0) == "Fibonacci, Square, Triangular"
    # Justification: 0 is part of Fibonacci, is a square (0^2), and is triangular (0th triangular number).
    
    # Test case 2: n = 1 (Edge case for all series)
    assert check_mathematical_series(1) == "Fibonacci, Square, Triangular"
    # Justification: 1 is part of Fibonacci, is a square (1^2), and is triangular (1st triangular number).
    
    # Test case 3: n = 2 (Fibonacci only)
    assert check_mathematical_series(2) == "Fibonacci"
    # Justification: 2 is Fibonacci but not square or triangular.
    
    # Test case 4: n = 3 (Fibonacci and Triangular)
    assert check_mathematical_series(3) == "Fibonacci, Triangular"
    # Justification: 3 is Fibonacci and triangular (2nd triangular number) but not a square.
    
    # Test case 5: n = 4 (Square only)
    assert check_mathematical_series(4) == "Square"
    # Justification: 4 is a square (2^2) but not Fibonacci or triangular.
    
    # Test case 6: n = 5 (Fibonacci)
    assert check_mathematical_series(5) == "Fibonacci"
    # Justification: 5 is Fibonacci but not square or triangular.
    
    # Test case 7: n = 6 (Triangular)
    assert check_mathematical_series(6) == "Triangular"
    # Justification: 6 is triangular (3rd triangular number) but not Fibonacci or square.
    
    # Test case 8: n = 7 (None)
    assert check_mathematical_series(7) == "None"
    # Justification: 7 is not part of any series.
    
    # Test case 9: n = 8 (Fibonacci)
    assert check_mathematical_series(8) == "Fibonacci"
    # Justification: 8 is Fibonacci but not square or triangular.
    
    # Test case 10: n = 9 (Square)
    assert check_mathematical_series(9) == "Square"
    # Justification: 9 is a square (3^2) but not Fibonacci or triangular.
    
    # Test case 11: n = 10 (Triangular)
    assert check_mathematical_series(10) == "Triangular"
    # Justification: 10 is triangular (4th triangular number) but not Fibonacci or square.
    
    # Test case 12: n = 21 (Fibonacci and Triangular)
    assert check_mathematical_series(21) == "Fibonacci, Triangular"
    # Justification: 21 is Fibonacci and triangular (6th triangular number).
    
    # Test case 13: n = 17 (None)
    assert check_mathematical_series(17) == "None"
    # Justification: 17 is not part of any series.
    
    print("All tests passed.")

# Run tests 
test_check_mathematical_series()