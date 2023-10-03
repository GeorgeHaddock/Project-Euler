# -*- coding: utf-8 -*-
"""
--------------------- TITLE ------------------------
Project Euler: Mathematical problem-solving by computer 
---- Problem 6: Sum Square Difference ----
----------------------------------------------------

------- Author(s) --------
George Haddock - UID: 10278321 - george.haddock@student.manchester.ac.uk

---- File Description ----


----------------------------------------------------
Created:    22/09/23
Last Saved: 

"""
sum_square = 0
square_sum = 0
for n in range(1,101):
    sum_square += n**2
    square_sum += n

square_sum **= 2

diff = square_sum - sum_square

print(diff)
