def anagram(n1: int, n2: int) -> bool:
    freq = [0] * 10
    anagram=True
    while n1!= 0:
        rem = n1%10
        freq[rem] += 1
        n1 //=10

    while n2!=0:
        rem = n2%10
        freq[rem] -=1
        n2//=10

    for i in freq:
        if i != 0:
            
            anagram= False
    if anagram:
        print("anagram")
    else:
        print("not")   

x = anagram(133,321)
