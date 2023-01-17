#!/usr/bin/python3

import sys
import numpy
import matplotlib.pyplot as plt

while True:

    a = input("Enter the value for a: ")
    b = input("Enter the value for b: ")
    c = input("Enter the value for c: ")

    try: 
        a = float(a)
        b = float(b)
        c = float(c)
        break

    except Exception as e:
        print(e)

###########################
# Constructing the equation
###########################

if a >= 0:
    avalue = str(a)
    avalue = avalue.strip()
    avalue = "{}".format(avalue)

else: 
    avalue = str(a)
    avalue = avalue.strip("-")
    avalue = avalue.strip()
    avalue = "- {}".format(avalue)

if b >= 0:
    bvalue = str(b)
    bvalue = bvalue.strip()
    bvalue = "+ {}".format(bvalue)

else: 
    bvalue = str(b)
    bvalue = bvalue.lstrip("-")
    bvalue = bvalue.strip()
    bvalue = "- {}".format(bvalue)

if c >= 0:
    cvalue = str(c)
    cvalue = cvalue.strip("-")
    cvalue = cvalue.strip()
    cvalue = "+ {}".format(cvalue)

else: 
    cvalue = str(c)
    cvalue = cvalue.strip("-")
    cvalue = cvalue.strip()
    print(cvalue)
    cvalue = "- {}".format(cvalue)

print(bvalue)
equation = "{}x² {}x {}".format(avalue, bvalue, cvalue)
print("\nYour equation: {}\n".format(equation))

##############################################
# Calculating the intersection with the x-axis
##############################################

D = (b**2)-4*a*c

if D == 0:
    x1 = (-b) / (2 * a)
    result = 1

elif D < 0:  
    result = 0 

elif D != 0:
    x1 = (-b + numpy.sqrt(D)) / (2 * a)
    x2 = (-b - numpy.sqrt(D)) / (2 * a)
    result = 2

###################
# Generating result
###################

if result == 0:
    print("No intersections with the x-axis.")
    sys.exit("")

elif result == 1:
    print("Intersection with the x-axis at [{}, 0].".format(x1))
    crd1 = x1 - 2
    crd2 = x1 + 2

elif result == 2:
    print("Intersection with the x-axis at [{}, 0] and [{}, 0].".format(x1, x2))

    maximum = max(x1, x2)
    minimum = min(x1, x2)

    crd1 = minimum - 2
    crd2 = maximum + 2

print("")

################
# Drawing a plot
################

xCoordinates = [i for i in numpy.arange(crd1, crd2, 0.1)]
xAxis = [0 for i in numpy.arange(crd1, crd2, 0.1)]
yCoordinates = []

for i in numpy.arange(crd1, crd2, 0.1):
    yValue = (a * (i**2)) + b * i + c
    yCoordinates.append(yValue)

# Actual graph
plt.plot(xCoordinates, yCoordinates)

# X-axis
plt.plot(xCoordinates, xAxis)
plt.ylabel("y")
plt.xlabel("x")
plt.title("Intersections with the x-axis".format(equation))

figure = plt.gcf()
figure.savefig("quadraticEquation.jpg")