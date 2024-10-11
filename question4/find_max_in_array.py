def largest(arr, n):
    # Check for empty array
    if n == 0:
        return -1  # Or you could return None to signal no valid result
    
    # Initialize the maximum element
    current_max = arr[0]

    # Traverse array elements from the second and compare with the current maximum
    for i in range(1, n):
        if arr[i] > current_max:
            current_max = arr[i]
    
    return current_max
