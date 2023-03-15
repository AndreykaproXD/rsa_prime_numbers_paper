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


def generator_e(p,q):
    e=random.choice(primes)
    while e>=p or e>=q:
        e=random.choice(primes)
    print(e)
    return e


def generator_d(p,q,e):
    d=random.choice(primes)
    while (e*d)%f_n!=1:
        d=random.choice(primes)
    print(d)
    return d

def alphabet():
    rus = dict()
    for i in range (1,33):
        rus.update({chr(i+1039):i})
    return (rus)

def code(rus):
    i = str(input("Введите русскую заглавную букву:"))
    x=rus.get (i)
    print(x)
    y=(x**e)%f_n
    return y

def decode(y):
    z=(y**d)%f_n
    return z



primes = []
primes = prime(int(input("Введите диапазон простых чисел:")))
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
e=generator_e(p,q)
d=generator_d(p,q,e)
print("e=",e)
print("d=",d)
abc=alphabet()
coded_num=code(abc)
decoded_num=decode(coded_num)
print("Закодированное число -",coded_num)
print("Расшифрованное число -",decoded_num)
