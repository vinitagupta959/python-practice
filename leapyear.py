year=int(input("enter year"))
result="not a leap year"
if year%400==0:
    result="Leap year"
else:
    if year%4==0:
        if year%100!=0:
            result="Leap year"
print(result)