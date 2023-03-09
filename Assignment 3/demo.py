import os  
# create the cities folder if it doesn't exist 
if not os.path.exists('cities'):   
      os.makedirs('cities')  
# list to store the cities 
cities = []  
# ask the user for cities 
while True:   
      city = input("Enter a city (press Enter to stop): ")  
      if city == '':     
            break   
      cities.append(city)  
# create a file for each letter and write the cities starting with that letter to the file 
for city in cities:   
      first_letter = city[0].upper()   
      with open(f"cities/{first_letter}.txt", 'a') as f:     
            f.write(f"{city}\n") 
