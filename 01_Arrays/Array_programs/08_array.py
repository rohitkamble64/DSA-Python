# write a function to print all the unique elements in an array

def unique(arr):
    unique_elements = []
    for num in arr:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements

arr = [1, 2, 3, 2, 4, 5, 1, 6]
unique_arr = unique(arr)
print(f"Unique Elements are: {unique_arr}")