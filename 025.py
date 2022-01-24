def fibo(x):
    if x==1 or x==2:
        return 1
    
    return (fibo(x-1)+fibo(x-2))

def nbdigit(n):
    nbd=0
    while n>1:
        n=n/10
        nbd=nbd+1
    return nbd

def euler025(maxi):
    i=1
    nbfib=0
    while nbdigit(fibo(i))<maxi:
        i=i+1      
    return i

print (euler025(1000))