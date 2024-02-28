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


