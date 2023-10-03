# -*- coding: utf-8 -*-
"""
--------------------- TITLE ------------------------
Project Euler: Mathematical problem-solving by computer 
---- Problem 5: Smallest Multiple ----
----------------------------------------------------

------- Author(s) --------
George Haddock - UID: 10278321 - george.haddock@student.manchester.ac.uk

---- File Description ----


----------------------------------------------------
Created:    22/09/23
Last Saved: 

"""
from collections import Counter
def find_factors(number):
    factor_list = []
    last_factor = 2
    while number > 1:    
        for n in range(last_factor, number+1):
            if number % n == 0:
                #print(str(number)+ "\n >> "+str(n))
                number //= n
                last_factor = n
                factor_list.append(n)
                break
            #print ('bing')
    return factor_list

multiples_factor_list = Counter()
for n in range(1,21):
   multiples_factor_list |= Counter(find_factors(n))

product = 1
for n in multiples_factor_list:
    product *= n**(multiples_factor_list[n])

print(product)
