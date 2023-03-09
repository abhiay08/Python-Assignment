"""_summary_



2.B.1: ASSIGNMENT

PROBLEM STATEMENT

Implement a python program that will input student details, marks in 5 subjects and calculates the percentage scored by student.

Requirements:

1. The program should ask the student for name and roll number.

Validate if name is a string and roll number is an integer, if not, show an error message saying “Invalid name/roll number” and ask for the value again after that.


2. Once you have the name and roll number the program should ask for score in 5 subjects in order: English, Hindi, Maths, Science, Social Science

Score must be within 1-100 otherwise show an error ‘Invalid score’ and ask for the subject score again.


3. After getting score for all the subjects calculate the percentage of student up to 2 decimal places and show the result in following format:


Format:

Roll no.: [Roll number]

Name: [Name]

------------------------------

English: [English score]

Hindi: [Hindi score]

… and similarly for other 3 subjects

------------------------------

Percentage: [Percentage]

Result: [Pass/Fail]


If the score is under 36% show the Result as Fail else show Pass.

END OF ASSIGNMENT
"""
#     1)validate name and roll number   
studname = input("\n Enter student name : \n")

rollnum=input("\n Enter your roll number : \n")

if studname.isalpha()==True & rollnum.isdigit()==True:
      
        st = studname
        rn=rollnum
else:
      
         print(" \n Invalid  Name/Roll number...!\n Please enter valid details\n")
         exit()

Python = int(input("\n Enter your Python subject score:\n"))
print("\nPython Score is:",+ Python)

Java = int(input("\nEnter your Java score:\n"))
print("\nJava Score is:",+ Java)

Django =int(input("\nEnter your Django subject score:\n"))
print("\nDjango Score is:",+ Django)

Perl =int(input("\nEnter your Perl subject score:\n"))
print("\n Perl Score is:",+ Perl)

PHP =int(input("\n Enter your php subject score:\n"))
print("\n PHP Score is:",+ PHP)

if Python.__le__(100) and Java.__le__(100)  and Django.__le__(100) and Perl.__le__(100) and PHP.__le__(100):
      
    py=Python
    java=Java
    django=Django
    perl=Perl
    php= PHP
    
    per = float((py + java + django + perl + php) / 500 * 100)
    
    p=round(per,2)
    
    print(p)
    
else:
    print("\n Invalid score....! Plase enter valid score details:")

if per>=75:
    print("Distinction..****..Congrulations...***!")
    
elif per>=60:
    print("First class.**Cheers for you.!")
    
elif per>=45:
    print("Second class..** You Have Successfully Scored GoodOne.!")
    
elif per>=37:
    print("Average.. *** Need ToTry More ***....!")
    
else:
    print("fail...** Better Try Next Time!**")






#rogh

# if English_score.__le__(100):
#   Es=English_score
#   print(Es)
# else:
#     print("invalid ")

