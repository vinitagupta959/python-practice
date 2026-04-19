word=input()
result=True
i=0
while i<len(word):
  if word[i]!="0" and   word[i]!="9":
    result=False
    break
  i+=1
print(result)