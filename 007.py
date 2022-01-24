def isprime(x):
    for i in range (2,x-1):
        if x%i==0:
            return False
    return True
    
#print(isprime(10001))

def euler007(maxi):
    x=0
    compteur=0
    while compteur<=maxi:
        x=x+1
        if isprime(x):
            compteur=compteur+1  
   
    return x

print(euler007(10001))