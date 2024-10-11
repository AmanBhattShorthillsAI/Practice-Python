def add(x,y):
    """addition of numbers"""
    return x+y

def subtract(x,y):
    """subtraction of numbers"""
    return x-y

def multiply(x,y):
    """multiplication of numbers"""
    return x*y

def divide(x,y):
    """division of numbers"""
    if y==0:
        raise ValueError('Cannot divide with zero!!')
    return x/y