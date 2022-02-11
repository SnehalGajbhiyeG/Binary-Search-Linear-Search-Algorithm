def binarySearch (arr,x,l,r):     # where a = array, x = data

    while(l<=r):
        
        mid = (l+r)//2 

        if x == arr[mid] :
            return mid 

        elif x > arr[mid] :
            l = mid + 1 

        else:
            r = mid - 1 

    return -1 

arr = [2,3,4,5,6,7,8,9] 
x = 6

result = binarySearch(arr,x,0,len(arr)-1)

if result != -1:
    print("Element of list at index,", str(result)) 

else:
    print("not found")  
    