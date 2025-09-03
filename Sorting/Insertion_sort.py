def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        insert_index=i
        current_value=arr.pop(i)
        for j in range(i-1,-1,-1):
            if arr[j]>current_value:
                insert_index=j
        arr.insert(insert_index,current_value)
    return arr

if __name__=='__main__':
    arr=[7,6,5,4,3]
    res=insertion_sort(arr)
    print("Sorted Array : ",res)