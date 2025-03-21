# OLD BUT GOLD!

import random 

class RSA:

    k = random.randint(50,100)

    def gen_primes(k):

        primes = []

        for i in range(2,k+1):
            divisors = []
            for j in range(1,i+1):

                if i%j == 0:
                    divisors.append(j)
            
            if len(divisors)==2:
                primes.append(i)

        print(f'k is {k} and the list of primes is:{primes}')

        p = random.choice(primes)

        q = random.choice(primes)

        while p==q:
            q = random.choice(primes)

        print(f'The values for p and q are {p,q}, respectively')

        return p,q 

    def n_totient_e(p,q):

        n = p*q 
        totient = (p-1)*(q-1)

        primes = []

        for i in range(2,totient):
            divisors = []
            for j in range(1,i+1):
                if i%j ==0:
                    divisors.append(j)
            if len(divisors) == 2:
                primes.append(i)

        e = random.choice(primes)

        while totient %e == 0:
            e = random.choice(primes.remove(e))

        print(f'The values of n, totient, and e : {n,totient,e}, respectively')

        return n, totient, e
    
    def encrypt(message, e, n):

        encryption = (message ** e) % n 

        print(f'The encryption result is: {message}^{e} mod {n} = {encryption}')
        print("{:b}".format(encryption))

        return encryption


y = RSA

k = y.k 

p,q = y.gen_primes(k)

n,totient, e = y.n_totient_e(p,q)

enc = y.encrypt(123, e, n)
