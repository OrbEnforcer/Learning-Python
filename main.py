#DAY 2
import mymodule
print(mymodule.info)
#Multiple variables in one line 
print(
    mymodule.name,
    mymodule.age,
    mymodule.height
)
#ZIP
print(mymodule.z1)
print(set(mymodule.a))

#Area of a circle 
from math import pi
print('Enter radius of circle in meters.')
r= int(input('Radius = ' ))
areaofcircle = pi*r**2
circumofcircle= 2*pi*r
print(
    'Area is ' + str(areaofcircle)
)
print(
    'Circumference is ' + str(circumofcircle)
)

#DAY 3

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
x = int(input("Enter x: " ))
y = 2 * x - 2

slope = y / x

print('Slope of the line y=2x-2 is ' + str(slope))

#Plots
import matplotlib.pyplot as plt
x1 = [1, 2, 3]
y1 = [0 ,2 ,4]

plt.plot(x1, y1)
plt.show()

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
print("In th given quadratic equation y=x²+6x+9, let's find the roots of the equation using input from the user. ")

x = int(input('Enter the value of x for which y will be 0: '))

y = x ** 2 + 6 * x + 9 

print(
    'At ' + str(x),
    'y is equal to ' + str(y)
)