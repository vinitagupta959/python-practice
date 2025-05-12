""" Given three integers representing the lengths of the sides of a triangle, determine whether these sides can form a valid triangle or not.
Triangle Validation Criteria:
A set of three side lengths can form a valid triangle if and only if the sum of the lengths of  two sides is greater than the length of the third side.

Input:
The input consists of a single line containing three space-separated integers representing the lengths of the sides of a triangle: a, b, and c (1 <= a, b, c <= 1000).
Output:
Print "YES" if the given sides can form a valid triangle, otherwise print "NO".
Constraints:
- 1 <= a, b, c <= 1000

Example:
Input:
3 4 5
Output:
YES

Explanation:
The given sides a = 3, b = 4 and c = 5 can form a valid triangle because the sum of any two sides is greater than the third side:
3 + 4 > 5
4 + 5 > 3
5 + 3 > 4
Therefore, the output is "YES".
 """
 
a,b,c=map(int, input().split())
if a+b>c and b+c>a and c+a>b:
    print("YEs")
else:
    print("No")