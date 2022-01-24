def fibo(x):
    if x==1 or x==2:
        return 1
    
    return (fibo(x-1)+fibo(x-2))
                    
                    
#print(fibo(7))

def Euler002(maxi):
    somme =0
    n=1
    while fibo(n)<maxi :
        if fibo(n)%2==1:
            somme= somme+fibo(n)
            print(fibo(n))
        n=n+1
    return somme

print (Euler002(4000000))