arr = [5,10,30,20,40,47]
pos = 3

for i in range(pos,len(arr)-1,1):
    arr[i] = arr[i+1]
arr[-1] = 0
    
print(arr)

