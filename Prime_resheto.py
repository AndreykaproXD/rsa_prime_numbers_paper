import random


def prime(N):
    n = [N for N in range (1,N+1)]
    n[0] = 0
    S = 2
    while S < N/2:
        if n[S-1]!=0:
            R = S+S
            while R<=N:
                n[R-1] = 0
                R = R+S
        S=S+1
    n = set(n)
    n.remove(0)
    n = list(n)
    return n


def check_e(e):
    return True


def check_d(d):
    return True

primes = []
primes = prime(int(input()))
print(primes)
p=random.choice(primes)
q=random.choice(primes)
while p==q:
    q=random.choice(primes)
print("p=",p)
print("q=",q)
n = p*q
print("n=",n)
f_n=(p-1)*(q-1)
print("f(n)=",f_n)
e=random.choice(primes)
while e==p or e==q and f_n:
    e=random.choice(primes)
d=random.choice(primes)
while check
while d==p or d==q or d==e:
    d=random.choice(primes)
print("e=",e)
print("d=",d)
