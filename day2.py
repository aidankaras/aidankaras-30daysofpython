# Day 2: 30 Days of Python programming
first_name = 'Aidan'
last_name = 'Karas'
full_name = first_name + ' ' + last_name
country = 'United States'
city = 'Boston'
age = 19
year = 2006
is_married = False
is_true = True
is_light_on = True
village, state, zip_code = 'Whitefish Bay', 'Wisconsin', 53217

print(type(village))
print(type(state))
print(type(zip_code))
print(type(full_name))
print(len(first_name))
print(len(last_name))
print(len(full_name))
print(first_name > last_name)

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

import numpy as np
radius = 30
area_of_circle = np.pi * radius**2
circumference_of_circle = 2 * np.pi * radius
def calculate_area(radius):
    area = np.pi * radius**2
    return area

input_r = input('Enter a radius:')
if float(input_r) <= 0 or float(input_r) is None:
    print('Please enter a positive number for the radius.')
else:
    print('Area:', calculate_area(float(input_r)))

first_name = input('Enter your first name:')
last_name = input('Enter your last name:')
full_name = first_name + ' ' + last_name
print('Your full name is:', full_name)

print(help('keywords'))
