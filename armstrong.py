""" An Armstrong number (also known as a narcissistic number, pluperfect number, or 
pluperfect digital invariant) is a number that is equal to the sum of its own digits 
each raised to the power of the number of digits.

Example: 153
number = 153
Number of digits = 3
Raise each digit to the power 3 and add them
1³ =   1
5³ = 125
3³ =  27

Step 3: Add the powered digits
1 + 125 + 27 = 153

Step 4: Compare the result with the original number
Since 153 == 153,
→ 153 is an Armstrong number """



# First way 
def checkArmstrong(n):
    num = n
    temp = n
    power = 0
    while temp > 0:
        temp //= 10
        power += 1
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        
        # Calculate digit^power using while loop
        mul = 1
        count = 0
        while count < power:
            mul *= digit
            count += 1
        total += mul
        temp //= 10
    return "Yes" if total == n else "No"
print(checkArmstrong(153))

# Time Complexity: O((log n)²)

# Is code me 3 loops hain — ek digits count karne ke liye O(log n), doosra digits extract karne ke liye O(log n), aur uske andar ek nested loop hota hai digit ki power calculate karne ke liye O(log n). Isliye total time complexity O((log n)² + log n) hoti hai. Lekin Big O notation me sirf sabse badi (dominant) complexity li jaati hai, isliye final answer hoga: O((log n)²)




# ye second type hai 
def checkArmstrong1(n):
    num=n 
    total=0
    power=len(str(n))
    while num>0:
        id=num%10
        total=total+(id**power)
        num=num//10
    return "Yes" if total == n else "No"
print(checkArmstrong(1534))
# Time Complexity: O(log n)

# We divide the number (num) by 10 in each iteration using num // 10,
# which means we are removing one digit in every step.
# The number of digits in 'n' is approximately log₁₀(n),
# so the loop runs log₁₀(n) times.
# In Big O notation, the base of the logarithm and constants are ignored,
# so we write it as O(log n), not O(log₁₀(n)) or log₁₀(n) + 1.

# and space com;exity is o(1) constent.