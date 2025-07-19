"""Problem Statement
You are given a positive integer num. Your task is to count the number of digits in num without converting it to a string.

Input:- 
A single integer num (1 ≤ num ≤ 10⁹)
Output
Print the number of digits in num"""

# We can solve this problem in two ways:
# 1. Without Using Any Built-in Method (Simple Loop)
# def countDigits(num):
#     count = 0
#     while num > 0:
#         num = num // 10
#         count += 1
#     return count
# num = int(input())
# print(countDigits(num))




# Using log10() from the math module
from math import *
def countDigits(num):
    return int(log10(num)+1)
    # log10(5558) = 3.7453 approx
    # Jab hum log10(n) nikalte hain, to hum dekhte hain ki n kis do 10 ki powers ke beech mein aata hai.
    # Example: 5558 lies between 10^3 = 1000 and 10^4 = 10000, so answer will be between 3 and 4.
    # Ab approximation ke liye:
    # Step 1: Lower power = 3, Higher power = 4
    # Step 2: log10(5558) ≈ 3 + (5558 - 1000) / (10000 - 1000)
    # Step 3: 3 + 4558 / 9000 = 3 + 0.5064 ≈ 3.5064
    # Lekin actual log10(5558) ≈ 3.7453 hota hai.
    # Approximation helpful hoti hai paper/pen se jaldi estimate karne ke liye.

# then We add 1 to log10(num) because the number of digits is always one more than the integer part of log base 10 of a number. Then we use int() to remove the decimal and get the final digit count.

print(countDigits(54563))



# Time Complexity: O(1) (Constant Time)
# log10() is a built-in function and performs in constant time.
# This method is faster and more efficient for large numbers.
