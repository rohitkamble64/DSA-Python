# This program finds the smallest and largest numbers in an array.
nums = [3, 5, 1, 8, 2]

smallest = float('inf')
largest = float('-inf')

for i in range(len(nums)):
    if nums[i] < smallest:
        smallest = nums[i]
    if nums[i] > largest:
            largest = nums[i]   

print(f"Smallest number is: {smallest} at index {nums.index(smallest)}")
print(f"Largest number is: {largest} at index {nums.index(largest)}") 
   