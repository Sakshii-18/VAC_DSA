n1 = 1221
n2 = 1212
isAnagram = False

freq = [0] * 10
freq2 = [0] * 10

while (n1!=0):
    rem = n1%10
    freq[rem] += 1
    n1 //=10
    
while (n2!=0):
    rem = n2%10
    freq2[rem] += 1
    n2 //=10
    
if freq == freq2:
    isAnagram = True
    
if isAnagram:
    print("Anagram")
else :    
    print("Not an Anagram")