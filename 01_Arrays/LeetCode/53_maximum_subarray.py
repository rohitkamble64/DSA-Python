'''
Leetcode Problem 53: Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''
#Using Kadane's Algorithm
nums = [-2,1,-3,4,-1,2,1,-5,4]
current_sum =0
max_sum = float('-inf') # Initialize max_sum to negative infinity

for val in nums:
    current_sum +=val
    max_sum = max(current_sum, max_sum)
    if current_sum < 0:
        current_sum = 0

print(f"The maximum subarray sum is: {max_sum}")