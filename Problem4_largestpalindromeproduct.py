# -*- coding: utf-8 -*-
"""
--------------------- TITLE ------------------------
Project Euler: Mathematical problem-solving by computer 
---- Problem 4: Largest Palindrome Product ----
----------------------------------------------------

------- Author(s) --------
George Haddock - UID: 10278321 - george.haddock@student.manchester.ac.uk

---- File Description ----


----------------------------------------------------
Created:    21/09/23
Last Saved: 

"""
import math 

def separate_digits(number):
    highest_digit = int(math.log10(number))
    digit_list = []
    for n in range(highest_digit+1):
        digit = (number // 10**n) % 10
        digit_list.append(digit)
    return digit_list[::-1]

palindrome_list = []
for n in range(100,1000):
    for m in range(100,1000):
        product = n*m
        digit_list = separate_digits(product)
        if digit_list == digit_list[::-1]:
            palindrome_list.append((product,n,m))

print(max(palindrome_list))
