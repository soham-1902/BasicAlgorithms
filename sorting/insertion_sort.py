def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        temp = arr[i]
        j = i-1
        
        while arr[j] > temp and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j+1] = temp
    return arr

# Example usage
array = [5, 3, 8, 4, 2]
sorted_array = insertion_sort(array)
print(sorted_array)
