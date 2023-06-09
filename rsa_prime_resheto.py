import random


def prime(prime_span):
    prime_arr = [prime_span for prime_span in range (1,prime_span+1)]
    # Use 0 for "stabbing out" all composite nums
    prime_arr[0] = 0
    S = 2
    while S < prime_span/2:
        if prime_arr[S-1]!=0:
            R = S+S
            while R<=prime_span:
                prime_arr[R-1] = 0
                R = R+S
        S=S+1
    prime_arr = set(prime_arr)
    prime_arr.remove(0)
    prime_arr = list(prime_arr)
    return prime_arr


def generator_e(p,q,f_n):
    e=random.choice(primes)
    while e>=f_n or e==p or e==q:
        e=random.choice(primes)
        print("e=",e)
    return e


def generator_d(e,f_n):
    c=1
    while 1:
        d=round((c*f_n+1)/e)
        c+=1
        mod_div_rem=(d*e)%f_n
        print("d=",d,"; mod_div_rem=", mod_div_rem)
        if mod_div_rem==1:
            break
    return d

def alphabet():
    rus = dict()
    for i in range (1,33):
        rus.update({chr(i+1039):i})
    return (rus)

def code(rus,e,n,ltr):
    x=rus.get(ltr)
    print("Порядок в алфавите(код символа): ",x)
    y=(x**e)%n
    return y

def decode(y,d,n):
    z=(y**d)%n
    return z



primes = []
primes = prime(int(input("Введите диапазон простых чисел:")))
print(primes)
rsa_p=random.choice(primes)
rsa_q=random.choice(primes)
#rsa_p=23
#rsa_q=37
while rsa_p==rsa_q:
    rsa_q=random.choice(primes)
rsa_n = rsa_p*rsa_q
rsa_f_n=(rsa_p-1)*(rsa_q-1)
rsa_e=generator_e(rsa_p,rsa_q,rsa_f_n)
#rsa_e=7
print("p=",rsa_p)
print("q=",rsa_q)
print("n=",rsa_n)
print("f(n)=",rsa_f_n)
print("e=",rsa_e)
rsa_d=generator_d(rsa_e,rsa_f_n)
print("d=",rsa_d)
if rsa_e==rsa_d:
    print("Ошибка: публичный и приватный ключи равны. Шифр нестойкий.")
else:
    abc=alphabet()
    rus_word = str(input("Введите слово из русских заглавных букв:"))
    for rus_letter in rus_word:
        coded_num=code(abc,rsa_e,rsa_n,rus_letter)
        decoded_num=decode(coded_num,rsa_d,rsa_n)
        if abc[rus_letter]==decoded_num:
            print("Символ: ",rus_letter, "; шифр: ",coded_num,"; расшифровка: ",decoded_num,"\n")
        else:
            print("Ошибка: код буквы и расшифрованное число не равны")
