# THIS ONE WAS PLANNED TO BE USED WITH OOP CLASS BUT IT WAY CHANGE
def has_decimal_part(number):
    # Convert the number to a string
    num_str = str(number)

    # Check if there is a dot in the string
    if '.' in num_str:
        # Get the part of the string after the dot
        decimal_part = num_str.split('.')[1]

        # Check if the decimal part is not empty
        if decimal_part:
            return True
        else:
            return False
    else:
        return False

def ends_with(number, after_point):
    # Convert number to string
    num_str = str(number)
    
    # Construct the pattern for ends with
    pattern = ".{}"
    
    # Check if the last characters match the pattern
    if num_str.endswith(pattern.format(after_point)):
        return True
    else:
        return False
