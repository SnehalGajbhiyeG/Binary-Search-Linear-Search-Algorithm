def linearSearch(arr, x):

    for i in range(len(arr)):

        if arr[i] == x :
            return i 

    return -1 

arr = [1,8,3,5,4,7,9]
x = 7 

result = linearSearch(arr,x) 

if result != -1 :
    print("Element found at index",str(result))
else:
    print("Element not found") 