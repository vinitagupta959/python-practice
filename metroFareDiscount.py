age=int(input())
baseFare=int(input())
fare=0
if age<5:
  fare=0
elif age>=5 and age<=12:
  fare=baseFare*50//100
elif age>=60:
  fare=baseFare*70//100
else:
  fare=baseFare
print(fare)