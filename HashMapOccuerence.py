n = 242130946884
freq = [0] * 10

while n!=0:
    rem = n%10
    freq[rem] += 1
    n //=10
    


for i in range(len(freq)):
    print(i, ":",freq[i])