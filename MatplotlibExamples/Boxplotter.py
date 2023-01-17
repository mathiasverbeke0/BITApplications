#!/usr/bin/python3

##################
# Imported modules
##################

import random
import matplotlib.pyplot as plt

######################
# Creating random data
######################

values = []

for i in range(0,5000):
    values.append(random.random())

values.append(1.5)

values2 = []

for i in range(0,5000):
    values2.append(random.random())
    
##################
# Making 1 boxplot
##################

plt.boxplot(values)
plt.title("1 boxplot")
plt.show()

############################################
# Making multiple boxplots next to eachother
############################################

collection = [values, values2]

plt.boxplot(collection, labels = (['values', 'values2']))
plt.title("Multiple boxplots with labels")
plt.xlabel("Values")
plt.show()

figure = plt.gcf()
figure.savefig("Scatterplot.jpg")