from sympy import totient
import math
import sys


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x-1):
        if x % i == 0:
            return False
    return True

# Take two numbers from the user
m=15
p = int(input("Enter first number: "))
q = int(input("Enter second number: "))
e=int(input("Enter public key:"))

# Check if the numbers are prime
print(f"{p} is {'a prime' if is_prime(p) else 'not a prime'} number.")
print(f"{q} is {'a prime' if is_prime(q) else 'not a prime'} number.")

#If any one of two numbers is not prime
if not is_prime(p):
    print(f"{p} is not a prime number. Exiting...")
    sys.exit()

if not is_prime(q):
    print(f"{q} is not a prime number. Exiting...")
    sys.exit()

n=p*q
print(f"value of n={n}")

phi_n = totient(n)
print(f"φ({n}) = {phi_n}")

if (math.gcd(phi_n,e)==1):
    for i in range (0,phi_n):
        if( ((phi_n*i)+1)%e==0):
            d= ((phi_n*i)+1)//e
            print(f"{d}  is a Private Key")
            break

  
c=((m^e)%n)
c = pow(m, e, n) 
print(f"Cipher text={c}")

p=((c^d)%n)
p=pow(c,int(d),n)
print(f"Decrypted Message ={p}")


