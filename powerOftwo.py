"""
 Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
"""





# if humee multiline coment karna ho to ctrl+shift+a use karte  hai 

# and question me hume boolen value  return karne ko bole hai or mai without  function bna rhi and print kara rhi true fals it's wrong
""" 
n=int(input("Enter a number: "))
if n==1:
    print("True")
elif n==0:
    print("False")
else:
    while n%2==0:
        n=n//2
    if n==1:
        print("True")
     """
     
     
     
def powerOFtwo():
    n=int(input())
    if n<=0:
        return False
    else:
        while n%2==0:
            n=n//2
        return n==1
print(powerOFtwo())