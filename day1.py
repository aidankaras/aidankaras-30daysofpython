import sys
print(sys.version)

print(3+4) #addition
print(3-4) #subtraction
print(3*4) #multiplication
print(3/4) #division
print(3//4) #floor division
print(3%4) #modulus
print(3**4) #exponentiation

print('Aidan')
print('Karas')
print('United States of America')
print('I am enjoying 30 days of python')

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Aidan'))
print(type('Karas'))
print(type('United States of America'))
print(type(True))
print(type({'Name': 'Aidan', 'Age': 19, 'Country': 'United States of America'}))
print(type((1, 2, 3)))
print(type({1, 2, 3}))

import numpy as np
euclidean_distance = round(np.sqrt((2-10)**2 + (3-8)**2), 2)
print('euclidean_distance:', euclidean_distance)
