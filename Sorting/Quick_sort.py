def partition(arr,lb,ub):
    pivot=arr[lb]
    start=lb
    end=ub
    while start<end:
        while start < len(arr) and arr[start] <= pivot:
            start=start+1
        while arr[end]>pivot:
            end-=1
        if start<end:
            arr[start],arr[end]=arr[end],arr[start]
    arr[lb],arr[end]=arr[end],arr[lb]
    return end
def quicksort(arr,lb,ub):
    if lb < ub:
        loc=partition(arr,lb,ub)
        quicksort(arr,lb,loc-1)
        quicksort(arr,loc+1,ub)
    return arr

if __name__=='__main__':
    arr=[7,6,10,5,9,2,1,15,7]
    res=quicksort(arr,0,len(arr)-1)
    print("Sorted Array: ",res)