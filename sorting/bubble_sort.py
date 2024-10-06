def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track whether any swaps happen
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps, array is sorted
        if not swapped:
            break
    return arr

# Example usage
array = [5, 3, 8, 4, 2]
sorted_array = bubble_sort(array)
print(sorted_array)
