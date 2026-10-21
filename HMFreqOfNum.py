#print array of numbers whose freq is greater than 3

def Freq(n,k):
    freq = [0] * 10
    a = []
    
    while n!=0:
        rem = n%10
        freq[rem] += 1
        n //=10
        
    for i in range(len(freq)):
        if freq[i] >k:
            a.append(i)
            
    return a

n = 3214442423332
k = 3

res = Freq(n,k)

print(res)