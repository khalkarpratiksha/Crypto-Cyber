import math
import sys

#prime num
p=int(input("Enter the prime number:"))
#primitive_root
g=int(input("Enter the primitive root:"))

#select private key for alice :xa
Xa=int(input("Enter the private key for Xa:"))

#select private key for bob :Xb
Xb=int(input("Enter the private key for Xb:"))

def less_than_prime(x):
    if x >p:
        return False
    
    return True

# Check if the private_keys  are less than prime
print(f"{Xa} is {'Xa prime' if less_than_prime(Xa) else 'not a prime'} number.")
print(f"{Xb} is {'Xb prime' if less_than_prime(Xb) else 'not a prime'} number.")
if not less_than_prime(Xa):
    print(f"{Xa} is not less than prime number. Exiting...")
    sys.exit()

if not less_than_prime(Xb):
    print(f"{Xb} is not less thanv prime number. Exiting...")
    sys.exit()



#calculate the public key for Xa
Ya=(pow(g,Xa,p))
print(f"The public key for Xa is:{Ya}")


#calculate the public key for Xb
Yb=(pow(g,Xb,p))
print(f"The public key for Xb is:{Yb}")


#calculate the shared secret key for a Ka:
Ka=(pow(Yb,Xa,p))
print(f"The shared secret key for Xa is:{Ka}")

#calculate the shared secret key for b Kb:
Kb=(pow(Ya,Xb,p))
print(f"The shared secret key for Xb is:{Ka}")