# write a function to calculate sum & product of all elements in an array

def sum_product(arr):
    sum = 0
    product = 1

    for num in arr:
        sum += num
        product *=num

    return sum, product

arr = [1, 2, 3, 4, 5]
result = sum_product(arr)
print(f"Sum of elements: {result[0]}")
print(f"Product of elements: {result[1]}")