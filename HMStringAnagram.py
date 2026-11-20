def anagram(s1,s2):
    freq = {}
    for i in s1:
        if i in freq :
            freq[i] += 1
        else:
            freq[i] = 1
    
    for i in s2:
        if i in freq :
            freq[i] -=1
        else:
            freq[i] =1
        
    for i in freq:
        if freq[i] != 0:
            return False
    return True

x = anagram("eat","taa")
print(x)