arr = [1, 2, 3, 4, 5]
n = len(arr)

max_sum = float('-inf') # Initialize max_sum to negative infinity

for start in range(n):
    current_sum = 0 
    for end in range(start, n):
        current_sum += arr[end] # Add the current element to current_sum
        max_sum = max(current_sum, max_sum) # Update max_sum if current_sum is greater

print(f"The maximum subarray sum is: {max_sum}")
    