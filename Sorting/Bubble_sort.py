arr=[7, 3, 9, 12, 11]

size=len(arr)
for i in range(size-1):
    swapped=False
    for j in range(size-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped=True
        if not swapped:
            break

print("Sorted Array: ",arr)