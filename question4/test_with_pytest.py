from find_max_in_array import largest

def test_with_regular_input():
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert largest(arr, len(arr)) == 9
    
def test_with_negative_input():
    arr = [-9, -8, -7, -6, -5, -4, -3, -2, -1]
    assert largest(arr, len(arr)) == -1
    
def test_with_duplicates():
    arr = [9, 8, 9, 7, 3]
    assert largest(arr, len(arr)) == 9
    
def test_with_empty_array():
    arr = []
    assert largest(arr, len(arr)) == -1
    
def test_with_single_element_array():
    arr = [42]
    assert largest(arr, len(arr)) == 42
    
def test_with_all_elements_equal():
    arr = [2, 2, 2, 2, 2]
    assert largest(arr, len(arr)) == 2
    
def test_with_both_positive_and_negative():
    arr = [-10, 4, -3, 98, -99]
    assert largest(arr, len(arr)) == 98
    
def test_with_largest_numbers():
    arr = [1000000000, 999999999, 1234567890, 9876543210]
    assert largest(arr, len(arr)) == 9876543210
    
