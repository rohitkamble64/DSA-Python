# write a function to swap the max and min elements in an array
def swap_max_min(arr):
    if not arr:
        return arr
    
    max_value = max(arr)
    min_value = min(arr)
    max_index = arr.index(max_value)
    min_index = arr.index(min_value)

    arr[max_index], arr[min_index] = arr[min_index], arr[max_index]

    return arr

arr = [13, 5, 11, 8, 2]
swapped_arr = swap_max_min(arr)
print(f"Array after swapping max and min elements: {swapped_arr}")