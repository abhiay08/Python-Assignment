# 3. Odd Number upto N
a=int(input("Enter a Lowest Digit: "))
b=int(input("Enter a Highest Digit: "))
for i in range(a,b+1):
    if (i% 2 == 1):
     print(i)
