"""Question: Find All Factors of a Number
Problem Statement:
Write a program to find and return all the factors of a given number.

Input:
A single integer num (1 ≤ num ≤ 10⁶)

Output:
A list containing all the factors of num in increasing order.
"""
# first way brute force
def factorsDivisor1(num):
    result=[]
    for i in range(1, num+1):
        if num%i==0:
            result=result+[i]
    return result

print(factorsDivisor1(10))


"""Time Complexity:
The loop runs from 1 to num, so the time complexity is O(n).For each i, we check num % i == 0 which is a constant-time operation.So total: O(n)
"""

"""Space Complexity:
Jab hum result list banate hain, to chahe vo ek hi variable ke andar ho, uske andar jo data store hota hai, uske liye memory alag se allocate hoti hai. result ek array (list) hai jo dynamically grow karti hai, aur ye kitni memory legi, ye is baat pe depend karta hai ki number ke kitne factors milte hain. Kabhi factors kam honge (jaise prime numbers ke), toh memory usage kam hoga, aur kabhi factors zyada honge (jaise 100 ke), toh zyada memory lagegi. Isliye space complexity O(k) hoti hai, jahan k total number of divisors hai. Yani, list bhale hi ek variable me ho, lekin uske andar ka data alag memory block me store hota hai, aur is wajah se uska size constant nahi hota. Ye cheez space complexity nikalte waqt dhyan me rakhni chahiye."""



"""second way
In the second approach, we observed that most of the factors of a number lie between 1 and num // 2. This is because no number greater than num // 2 (except the number itself) can divide num. For example, for num = 6, its factors are: 1, 2, 3, and 6. So we can run the loop only till num // 2, and finally add num to the list (since every number is divisible by itself)."""
def factorsDivisor2(num):
    result=[]
    for i in range(1, num//2+1):
        if num%i==0:
            result=result+[i]
    result=result+[num]
    return result
print(factorsDivisor1(20))




# optimise way
from math import sqrt
def factorsDivisor3(num):
    result=[]
    squrt=int(sqrt(num))
    for i in range(1, squrt+1):
        if num%i==0:
            result=result+[i]
            if num//i!=i:
                result=result+[num//i]
    result.sort() #if hum sorted chahate hao to 
    return result
print(factorsDivisor3(144))

# Time Complexity: O(√n log n) (due to sorting)
# Space Complexity: O(k) (k = number of factors stored)
