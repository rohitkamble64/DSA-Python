# This program prints all the subarrays of a given array.
arr = [1, 2, 3, 4, 5]
n = len(arr)

for start in range(n):
    for end in range(start, n):
        for i in range(start, end + 1):
            print(arr[i], end="")
        print(" ", end="")

    print()