arr=[7, 3, 9, 12, 11]

size=len(arr)

for i in range(size):
    min_index=i
    for j in range(i+1,size):
        if arr[min_index]>arr[j]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]

print('Sorted Array : ',arr)