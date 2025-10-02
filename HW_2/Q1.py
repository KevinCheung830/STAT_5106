import numpy as np
from typing import List, Tuple
# user_input = input("Enter 6 unique numbers between 1 and 49, separated by spaces: ")
# user_numbers = [int(num) for num in user_input.strip().split()]

def validate_entries(entry: List[int]) -> bool:
    """
    Validate a single Mark 6 entry.
entry: List of 6 unique integers between 1 and 49
    
    Returns:
        True if valid, False otherwise
    """
    try:
        if not isinstance(entry, list):
            raise ValueError("Entry must be a list")
        if len(entry) != 6:
            raise ValueError("Entry must contain exactly 6 numbers")
        if len(set(entry)) != 6:
            raise ValueError("Entry numbers must be unique")
        for number in entry:
            if not isinstance(number, int) or not (1 <= number <= 49):
                raise ValueError("Each number must be an integer between 1 and 49")
        return True
    except Exception as e:
        print(f"Error in validate_entries: {e}")
        return False
#print("Your entry is valid:", user_numbers) if validate_entries(user_numbers) else print("Invalid entry. Please try again.")

# simulate_draw() → generate 7 numbers → subseting first 6 and last 1 , sort the first 6
def simulate_draw() -> Tuple[np.ndarray, int]:
    np.random.seed(1834633)  
    #np.random.seed(2834633)  
    # generate 7 numbers
    numbers = np.random.choice(np.arange(1, 50), size=7, replace=False)
    # subseting first 6 and last 1 , sort the first 6 and format the output
    first_six = np.sort(numbers[:6])
    extra_number = int(numbers[-1])
    sorted_six = np.sort(first_six)
    return (sorted_six.tolist(), extra_number)

def calculate_prize(entry_numbers: List[int], draw: Tuple[List[int], int]):
    """
    Calculate the prize for a Mark 6 entry.
    
    Args:
        entry_numbers: List of 6 user-chosen numbers
        draw: Tuple of (drawn 6 numbers as list, extra number as int)
    
    Returns:
        Tuple: (prize_name, prize_amount, matching_count)
    """
    # tuple unpacking of draw drawn_numbers_six and extra_number
    drawn_numbers_six, extra_number = draw
    matching_numbers = set(entry_numbers) & set(drawn_numbers_six)
    matching_count = len(matching_numbers)
    extra_matched = extra_number in entry_numbers

    # Prize logic according to Mark 6 rules
    if matching_count == 6:
        return "1st prize", 61448360, matching_count
    elif matching_count == 5 and extra_matched:
        return "2nd prize", 498020, matching_count
    elif matching_count == 5:
        return "3rd prize", 38980, matching_count
    elif matching_count == 4 and extra_matched:
        return "4th prize", 9600, matching_count
    elif matching_count == 4:
        return "5th prize", 640, matching_count
    elif matching_count == 3 and extra_matched:
        return "6th prize", 320, matching_count
    elif matching_count == 3:
        return "7th prize", 40, matching_count
    else:
        return "No prize", 0, matching_count


# test
entry_1 = [2, 5, 14, 15, 39, 48]
validate_entries(entry_1)
draw = simulate_draw()
print(f"Draw: {draw}")
calculate_prize(entry_1, draw)
print(f"Prize Info: {calculate_prize(entry_1, draw)}")
