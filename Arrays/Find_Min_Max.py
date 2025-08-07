# Find Minimum and Maximum Element of the array

arr=[1,3,5,7,2,4]
min=max=arr[0]

for i in arr:
    if i<min:
        min=i
    if i>max:
        max=i

print("Minimum="+str(min),", Maximum="+str(max))