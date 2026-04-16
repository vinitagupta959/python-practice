""" 
For today, Chef is out of town, and his evil son has taken over his bakery.

Normally, Chef sells his cakes for 100 rupees each. However, his son can be bribed with K rupees, to sell each cake for 60 rupees instead. Note that you have to pay this bribe only one time, not for each cake.

You want to buy 
N cakes from the bakery. You can choose whether to bribe Chef's son or not. What is the minimum cost of buying the N cakes.

Input Format
The first and only line contains 
2 integers - N and K, the number of cakes you need to buy, and the bribe amount.

Output Format
Output the minimum total cost of buying the N cakes.

 
Sample 1:
Input
5 100
Output
400 
"""



# cook your dish here
n,k=map(int, input().split())
withBribe=(n*60)+k
withoutBribe=n*100
if withoutBribe<withBribe:
    print(withoutBribe)
else:
    print(withBribe)