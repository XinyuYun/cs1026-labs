# Replace the placeholders with code and run the Python program

import math
#check if number is prime not overly efficient
def prime(n):
    if n==1 or n==0:
        return False
    for x in range(2,int(math.sqrt(n)+1)):
        if n%x == 0:
            return False
    return True

# Define the dictionary
dict ={}
# Define the sets
eset = set()    # Set of even numbers
oset = set()    # Set of odd numbers
thset = set()   # Set of multiples of 3
pset = set()    # Set of prime numbers

for x in range(0,20):
    if x % 2 == 0:
        Add x to the set of even numbers
    if x % 2 == 1:
        Add x to the set of odd numbers)
    if x % 3 == 0:
        Add x to the set of multiples of 3
    if prime(x):
        Add x to the set of prime numbers

Add the even set to the dictionary
Add the odd set to the dictionary
Add the set of multiples of 3 to the dictionary
Add the set of primes to the dictionary

for item in dict:
    print(item,dict[item])

