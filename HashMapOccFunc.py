def countFreq(n):
    freq = [0] * 10
    
    while(n!=0):
        rem = n%10
        freq[rem] +=1
        n //=10
        
    return freq

n = 648578605803170

res = countFreq(n)

for i in range(len(res)):
    if res[i] > 0:
        print(i, "-->" , res[i])