nums = [0,10,2,3,12,0,23]

j =0
for i in range(0,len(nums),1):
    if nums[i] != 0:
        Swap(nums[i],nums[j])
        j +=1