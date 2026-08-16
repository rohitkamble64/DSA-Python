#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

def singleNumber(nums):
    ans = 0
    for val in nums:
        ans ^= val
    return ans

nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # Output: 4