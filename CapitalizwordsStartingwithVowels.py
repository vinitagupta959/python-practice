""" Problem Statement:
Write a program that reads a sentence and capitalizes only those words that start with a vowel (a, e, i, o, u). Leave all other words unchanged. The comparison should be case-insensitive, but the original casing of non-vowel words should be preserved.

For example, "apple is tasty and orange" becomes "Apple Is tasty and Orange".

Constraints:

Do not use for loops or for-in statements. Use only while loops to process characters.

Do not use built-in functions like split(), capitalize(), title(), or list comprehensions.

Do not use the while...else construct.

 """



# word=input()
# i=0
# newS=""
# lowelVowels="aeiou"
# upperVowel="AEIOU"
# while i<len(word):
#   if i==0 or word[i-1]==" ":
#     j=0
#     found=False
#     while j<len(lowelVowels):
#       if word[i]==lowelVowels[j] or word[i]==upperVowel[j]:
#         newS+=upperVowel[j]
#         found=True
#         break
#       j+=1
#     if found==False:
#       newS+=word[i]
#   else:
#     newS+=word[i]
#   i+=1
# print(newS)

word = input()
i = 0
newS = ""

while i < len(word):
    if i == 0 or word[i-1] == " ":
        if word[i] == 'a' or word[i]=="A":
            newS += 'A'
        elif word[i] == 'e'or word[i]=="E":
            newS += 'E'
        elif word[i] == 'i' or word[i]=="I":
            newS += 'I'
        elif word[i] == 'o' or word[i]=="O":
            newS += 'O'
        elif word[i] == 'u' or word[i]=="U":
            newS += 'U'
        else:
            newS += word[i]
    else:
        newS += word[i]
    i += 1

print(newS)