'''
Write a Python Script to conatenate following dictionary to create a new one.
'''
a={ 2:21, 5:51 }
b={ 3:31, 6:61}
c={4:41}
d={ 8:81,7:71}
print(type(a))
my_dict={}
my_dict.update(a)
my_dict.update(b)
my_dict.update(c)
my_dict.update(d)
print(my_dict)
