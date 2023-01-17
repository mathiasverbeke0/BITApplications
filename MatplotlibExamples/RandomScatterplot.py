#!/usr/bin/python3

##################
# Imported modules
##################

import random
import matplotlib.pyplot as plt

######################
# Creating random data
######################

xValues = []
yValues = []

for i in range(0,500):
    xValues.append(random.random())
    yValues.append(random.random())

xValues2 = []
yValues2 = []

for i in range(0,500):
    xValues2.append(random.random())
    yValues2.append(random.random())

########################
# Making the scatterplot
########################

plt.scatter(xValues, yValues, color = "hotpink")
plt.scatter(xValues2, yValues2, color = "lime")

figure = plt.gcf()
figure.savefig("Scatterplot.jpg")