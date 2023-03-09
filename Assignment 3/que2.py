''' 
Write a program Takes a list of cities as input (ask user if they want to add more city after each entry i.e. once user presses ‘Enter’)
Creates a folder in pwd (present working directory) named ‘cities’, then creates a file with names as first characters of cities and write the names of all the cities starting with that character
Example: User input: Bangalore, Mumbai, Ajmer, Alwar, Banaras, Chittor, Chennai
Then the present working directory must have: Cities(directory/folder)
-> A.txt
-> Ajmer
-> Alwar
-> B.txt
-> Bangalore
-> Banaras
-> C.txt
-> Chittor
-> Chennai
-> M.txt
-> Mumbai
I.e. Files named A,B,C and M.txt and each of them contain respective city names separated by newline (don’t include the ‘->’ it is used here to denote new line 
'''

import os

if not os.path.exists('cities'):
      os.mkdir("cities")
      cities=[]
while True:
      city=input('Enter a City: ')
      if city=="":
            break
      cities.append(city)
      
      print("Successfully Created")
      first_char=city[0]
      with open(f'cities/{first_char}.txt',"a")as f:
            f.write(city+'\n')