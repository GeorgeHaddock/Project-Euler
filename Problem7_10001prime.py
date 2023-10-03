# -*- coding: utf-8 -*-
"""
--------------------- TITLE ------------------------
Project Euler: Mathematical problem-solving by computer 
---- Problem 7: 10001th Prime ----
----------------------------------------------------

------- Author(s) --------
George Haddock - UID: 10278321 - george.haddock@student.manchester.ac.uk

---- File Description ----


----------------------------------------------------
Created:    25/09/23
Last Saved: 

"""

def prime_sieve(limit):
    smallest_prime = 2
    
    # Using Boolean Array
    prime_array = [True for i in range(limit+1)] # Or [True]*limit
    prime_array[0] = False #range end is exclusive
    prime_array[1] = False

    # Implementing sieve of Eratosthenes (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) 
    for i in range(2,limit+1):
        if prime_array[i] is True:
            for j in range(i**2,limit+1,i): #using i^2 to account for smaller multiples being filtered out already
                prime_array[j] = False

    return [i for i,prime_query in enumerate(prime_array) if prime_query]

print(prime_sieve(1000000)[10000])


    
    
    
    
    
    
    
    
    
    
    
    
    
    
   