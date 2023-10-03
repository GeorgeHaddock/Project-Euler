# -*- coding: utf-8 -*-
"""
--------------------- TITLE ------------------------
Project Euler: Mathematical problem-solving by computer 
---- Problem 2: Even Fibonacci Numbers ----
----------------------------------------------------

------- Author(s) --------
George Haddock - UID: 10278321 - george.haddock@student.manchester.ac.uk

---- File Description ----


----------------------------------------------------
Created:    21/09/23
Last Saved: 

"""
#Fibonacci Series

previous_term = 1
current_term = 2
next_term = 0

even_sum = 0

while previous_term < 4000000:
    print(previous_term)
    if previous_term % 2 == 0: even_sum += previous_term  
    next_term = current_term + previous_term
    previous_term = current_term
    current_term = next_term

print(even_sum)