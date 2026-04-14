word=input()
upperCase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerCase="abcdefghijklmnopqrstuvwxyz"
newS=""
i=0
while i<len(word):
    if word[i]=="a" or word[i]=="A" or word[i]=="e" or word[i]=="E" or word[i]=="i" or word[i]=="I" or word[i]=="o" or word[i]=="O" or word[i]=="u" or word[i]=="U":
        j=0
        while j<len(upperCase):
            if word[i]==upperCase[j]:
                newS+=upperCase[j+1]
            elif word[i]==lowerCase[j]:
                newS+=lowerCase[j+1]
            j+=1
    else:
        newS+=word[i]
    i+=1
print(newS)
