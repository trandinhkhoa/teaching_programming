print("Hello World")


### Variables
area = 25
PRICE_PER_SQUARE_METER = 100
print("Price of the lot =  ", area * PRICE_PER_SQUARE_METER)

area = 50
print("Updated Area = ", area)
print("Updated Price of the lot =  ", area * PRICE_PER_SQUARE_METER)

### Console/Terminal input
name = input("Enter your name: ")
print("Hello ", name)

### Conditional

# if <statement>: # True
#   <do something>
# else: # False
#   <do something>

# statement = statement1 and/or statement2 and/or statement3 ...

a_number = 10
if a_number == 0:
  print("Zero")
elif a_number % 2 == 0:
  print("Even number")
else:
  print("Odd number")

if a_number == 0:
  print("Zero")
elif a_number % 2 != 0:
  print("Odd number")
else:
  print("Even number")

age = input("Enter your age: ")
age = int(age)
print("Ya age = ", age)
if age > 30:
  print("Ya old")
else:
  print("Ya young")

### Functions

# PI = 3.14
# r = 3
# h = 2
# print("Volume of the cylinder = ", PI * r * r * h)
# h = 10
# print("Volume of the cylinder = ", PI * r * r * h)


def vol_cylinder(r, h):
  PI = 3.14
  vol = PI * r * r * h
  return vol

r = 3
h = 2
print("Volume of the cylinder = ", vol_cylinder(r,h))
h = 10
print("Volume of the cylinder = ", vol_cylinder(r,h))

#### Functions scope
a = 2
b = 3

def add(a,b):
  a = 10
  print("a = ", a)
  return a + b

print("a = ", a)
print("a + b = ", add(a,b))
print("a = ", a)

### Arrays and Loops

### FizzBuzz
n = int(input("Enter a number = "))
for i in range(1,n+1):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)
