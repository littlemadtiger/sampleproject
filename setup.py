#Welcome to the actual source file for the sample project. 
#In this project, I will be analyzing 3 different cities in the United States and their temperature variance between Celsius & Fahrenheit. 
#How would we know to convert between both? 
#How do we interpret the data presented? 
#Throughout the code, I will be illustrating how each sequence of code will correspond to the overall function of the program itself.
#Enjoy!



#Assigning a decorator/Illustrating what will wrap around our other function. 
def name_decorator(my_info):
  def wrapper(*args, **kwargs):  
    print("Introduction:\n")
    #Printing developer before our other function
    my_info(*args, **kwargs)
  return wrapper
 
#Assigning a general information about me func
@name_decorator
def my_info(name, age, birthPlace):
  print("Hi! My name is " + name + ". I'm " + str(age) + " years of age and originally from " + birthPlace + " and currently reside there.")
my_info("Jacob Sangiuliano", 21, "Aurora, Colorado")


#Return all new information/Store it and print it.
myInformation = name_decorator(my_info)
print(myInformation)

#Function for converting temperatures from Fahrenheit to Celsius
def city_variables_f(denver_temp_f, san_diego_temp_f, miami_temp_f):
  # Use equation: C = (F - 32)
  c_temp_denver = (denver_temp_f - 32) * 5 / 9
  c_temp_san_diego = (san_diego_temp_f - 32) * 5 / 9
  c_temp_miami = (miami_temp_f - 32) * 5 / 9
  #Display Fahrenheit temperatures
  print("These are the 3 cities temperature readings in Fahrenheit for July 4th, 2022:\n")
  print("Denver (f):\n" + str(denver_temp_f) + '\n' + "San Diego (f):\n" + str(san_diego_temp_f) + '\n' + "Miami (f):\n" + str(miami_temp_f) + '\n')
  #Display temperatures converted into Celsius
  print("The temperature readings in Celsius after conversion:\n")
  print("Denver (C):\n" + str(c_temp_denver) + '\n' + "San Diego (C):\n" + str(c_temp_san_diego) + '\n' + "Miami (C):\n" + str(c_temp_miami) + '\n')

#Returning set values
city_variables_f(74, 63, 84)
    
#TO BE CONTINUED
