from math import sqrt

def prime_list(n):
 sqrt_n = int(sqrt(n))
 no_primes = [j for i in range(2,sqrt_n) for j in range(i*2, n, i)]
 primes = [x for x in range(2, n) if x not in no_primes]
 return primes

def print_list(n):
     for x in n:
         print(x)
         
def ask():
 try: 
     n = int(input('What Number is your Max Number? : '))
     return n
 except ValueError:
     print('Oops Try Again!')
     ask()
 
print_list(prime_list(ask()))
