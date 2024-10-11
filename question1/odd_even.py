def check_even_odd(number):
    if not isinstance(number, int):
        raise TypeError('Input must be an integer')
    
    if number % 2 == 0:
        return f"{number} Is Even Number"
    else:
        return f"{number} Is Odd Number"
