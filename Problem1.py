# -*- coding: utf-8 -*-
"""
--------------------- TITLE ------------------------
Project Euler: Mathematical problem-solving by computer 
---- Problem 1: Sum of multiples of 3 & 5 up to 1000 ----
----------------------------------------------------

------- Author(s) --------
George Haddock - UID: 10278321 - george.haddock@student.manchester.ac.uk

---- File Description ----


----------------------------------------------------
Created:    21/09/23
Last Saved: 

"""

def find_and_sum(multiple, limit):
    sum = 0
    itteration_no = limit // multiple
    for n in range(itteration_no+1 if limit % multiple != 0 else itteration_no):
        sum += n*multiple   
    return sum

total = find_and_sum(3,1000) + find_and_sum(5,1000) - find_and_sum(15,1000)
print(total)