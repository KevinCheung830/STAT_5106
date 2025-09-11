import math

def is_triangular(x):
    # Given X is the number to check
    # Check if 8*x + 1 is a perfect square and if the square root is odd
    # If so , then it is a triangular number
    if x < 0: return False
    root = math.isqrt(8*x + 1)
    return root*root == 8*x + 1 and root % 2 == 1

# Test the function
test_numbers = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 2, 4, 7, 11, 100]
for num in test_numbers:
    result = is_triangular(num)
    print(f"{num}: {'Triangular' if result else 'Not triangular'}")

