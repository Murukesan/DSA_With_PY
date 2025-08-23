nums=[2,2,2,1,4,5]
mono=True
asc=False
desc=False
if len(nums)==1:
    mono=True
else:
    for i in range(0, len(nums) - 1, 1):
        if nums[i]==nums[i+1]:
            continue
        elif nums[i]>nums[i+1]:
            desc=True
        elif nums[i]<nums[i+1]:
            asc=True
    if desc:
        for i in range(0,len(nums)-1,1):
            if nums[i]<nums[i+1]:
                mono=False
    if asc:
        for i in range(0,len(nums)-1,1):
            if nums[i]>nums[i+1]:
                mono=False
print(mono)

