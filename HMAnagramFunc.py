def Anagram(n1,n2):
    freq = [0] * 10
    
    while n1!=0:
        rem = n1%10
        freq[rem] += 1
        n1 //=10
        
    while n2!=0:
        rem = n2%10
        freq[rem] -= 1
        n2 //=10
        
    for i in freq:
        if i!=0:
            return False
    return True


n1 = 1221
n2 =1122

res = Anagram(n1,n2)

print(res)        