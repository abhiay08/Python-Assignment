'''A. Using Dictionary'''
a={
      'name':"Abhi",
      'age':19
}
print(type(a))
b={
       'age':19,
       'name':'abhi'
 }
if a==b:
      print("\n Yes.....Dictionary is Equal")
else:
      print("\nNo....Dictionary are Not Equal")

"""B. Using Set"""

a = {1, 2, 3, 4, 5}
print(type(a))
b = {4, 5, 3, 1, 2}
if a == b:
    print("\nYes.....Set is Equals")
else:
    print("\n No......Set is Not Equal")
    
"""C. Using List"""

a = [1, 3, 5, 7, 9]
print(type(a))
b = [9, 7, 5, 3, 1]
if a == b:
    print("\nYes......List is Equal")
else:
    print("\nNo........List is Not Equal")

print("\nCode Created By ***Abhishek***")
