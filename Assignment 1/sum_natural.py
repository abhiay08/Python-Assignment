#4. Sum of Natural Number upto N
a=int(input("Enter the number: "))
if a<0:
    print("Please Enter a Positive Number")
else:
    sum=0
    while (a>0):
        sum+=a
        a-=1
        print("The sum is",sum)
