def binarysearch(arr,key):
    low=0
    high=len(arr)-1

    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==key):
            return mid
        elif(arr[mid]<key):
            low=mid+1
        else:
            high=mid-1

    return -1

myarray=[1,3,5,9,12,45,8]
key=91
result=binarysearch(myarray,key)

if(result!=-1):
    print("Value",key,"found at index",result)

else:
    print("Key not found in array")    
