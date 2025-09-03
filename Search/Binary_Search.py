def Binary_Search(arr,ele):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==ele:
            return mid
        elif arr[mid]>ele:
            right=mid-1
        else:
            left=mid+1
    return -1
if __name__=='__main__':
    arr=[1,2,3]
    res=Binary_Search(arr,ele=1)
    if res==-1:
        print("Element not found")
    else:
        print("Element fount at",res,"index")