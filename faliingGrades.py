""" 
🔢 Problem: Failing Grades
Chef took N total tests in his university, numbered 1 to N chronologically. Each test was graded out of 100 marks. He scored Ai marks in the i-th test.
Chef’s scholarship requires that his average score after each test remains at or above 40 marks.
You need to check for each test case if Chef was able to keep his scholarship throughout all the tests.

📥 Input Format:
The first line contains a single integer T — the number of test cases.

For each test case:
The first line contains an integer N — the number of tests.
The second line contains N space-separated integers — A₁, A₂, ..., Aₙ — Chef’s scores in each test.

📤 Output Format:
For each test case, print "Yes" if Chef was able to maintain an average of 40 or more after every test, otherwise print "No".
You may print the output in any case (i.e., "Yes", "YES", "yes" are all acceptable).

🔒 Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 100
0 ≤ Ai ≤ 100

input:- 
4
2
0 100
3
41 39 40
4
41 41 28 100
1
100

output:- 
No
Yes
No
Yes
"""


t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    i=0
    numbeTotalr=0
    sumNum=0
    result="Yes"
    while i<n:
        numbeTotalr+=1
        sumNum+=a[i]
        avrage=sumNum/numbeTotalr
        if (avrage)<40:
            result="No"
            break
        i+=1
    print(result)