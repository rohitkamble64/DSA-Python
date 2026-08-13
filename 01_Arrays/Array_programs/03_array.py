# pass by reference

def changeArr(arr):
    print("In function")
    for i in range(len(arr)):
        arr[i] = arr[i] * 2
    
arr = [1, 2, 3, 4, 5]

changeArr(arr)

print("Outside function")
print(arr)
# for i in range(len(arr)):
#     print(arr[i], end=" ")

