def linear_search(arr,ele):
    for i in arr:
        if i==ele:
            return True
    return False

arr=[1,2,3,4,5]
ele=4
res=linear_search(arr,ele)
if res==True:
    print("Element Found")
else:
    print("Element not found")