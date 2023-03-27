def minAmoeba(N): 
    if N == 1: 
        return 1 
    else: 
        if N % 2 == 0: 
            return minAmoeba(N // 2) 
        else: 
            return 1 + minAmoeba(N // 2) 
N = int(input()) 

print(minAmoeba(N)) 
