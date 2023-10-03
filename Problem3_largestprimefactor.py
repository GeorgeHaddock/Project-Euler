# -*- coding: utf-8 -*-
"""
--------------------- TITLE ------------------------
Project Euler: Mathematical problem-solving by computer 
---- Problem 2: Largest Prime Factor ----
----------------------------------------------------

------- Author(s) --------
George Haddock - UID: 10278321 - george.haddock@student.manchester.ac.uk

---- File Description ----


----------------------------------------------------
Created:    21/09/23
Last Saved: 

"""
def find_factors(number):
    factor_list = []
    last_factor = 2
    while number > 1:    
        for n in range(last_factor, number+1):
            if number % n == 0:
                print(str(number)+ "\n >> "+str(n))
                number = number // n
                last_factor = n
                factor_list.append(n)
                break
            #print ('bing')
    print(">>> It's been prime-d! It's prime factors are {0}.".format(factor_list))       
    return factor_list

find_factors(2520)
