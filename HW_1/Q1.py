def clean_number(number):
    """
    Removes any non-digit characters from the input.
    For example: '7992 7398-713' -> '79927398713'
    """
    return ''.join(filter(str.isdigit, str(number)))


def luhn_checksum(number):
    """
    Implements the Luhn algorithm to compute the checksum.
    Returns True if the checksum is valid (i.e., total % 10 == 0), False otherwise.
    """
    digits = [int(d) for d in number]
    checksum = 0
    # Start from the right, double every second digit
    for i in range(len(digits) - 2, -1, -2):  # -2 skips the check digit
        doubled = digits[i] * 2
        if doubled > 9:
            doubled -= 9
        digits[i] = doubled
    checksum = sum(digits)
    return checksum % 10 == 0


def validate_credit_card(number):
    """
    Validates a credit card number using the Luhn algorithm.
    Returns True if valid, False otherwise.
    """
    cleaned = clean_number(number)
    if not cleaned.isdigit() or len(cleaned) < 2:
        return False
    return luhn_checksum(cleaned)

print(validate_credit_card("79927398713"))  # True
print(validate_credit_card("1234 5678 9012 3456"))  # False
print(validate_credit_card("4012-8888-8888-1881"))  # True