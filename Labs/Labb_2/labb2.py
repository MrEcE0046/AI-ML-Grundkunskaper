import numpy as np, matplotlib.pyplot as plt, math

def distance_calc(data, test): # Spara distansen mellan test och data i en lista, returnera en lista.
    distance = []
    print(distance)
    for test in data:
        for i in test:
            distance = math.sqrt((data[0] - test[0])**2 + (data[1] - test[1])**2)
    return distance

pokemon = []
with open("datapoints.txt") as file:
    first_line = file.readline()
    for line in file:
        x = line.strip().split(",")
        pokemon.append(x)

pichu = [i for i in pokemon if i[2] == " 0"] # Sammlar alla pichu i en egen lista (alla som slutar på 0)
pichu = [i[:-1] for i in pichu] # Tar bort sista elementet i den inre listan (tar bort alla nollor)
picatchu = [i for i in pokemon if i[2] == " 1"]
picatchu = [i[:-1] for i in picatchu]

pichu = [[float(element) for element in i] for i in pichu] #GPT - konverterar str till float
picatchu = [[float(element) for element in i] for i in picatchu] # [23.43434, 21.43434]

x, y = zip(*pichu) 
x1, y1 = zip(*picatchu)

test = []
with open("testpoints.txt") as test_points: # Läser av testdata, rensar och placerar i lista
    first_line = test_points.readline()
    for line in test_points:
        t = line.split()
        test.append(t)

test = [i[1:] for i in test] # Tar bort index i början för alla inre listor
test = [[element.strip(",()") for element in i] for i in test] # Tar bort ', ' i dem inre listorna

test= [[float(element1) for element1 in i] for i in test]
x2, y2 = zip(*test)
print(test)
plt.scatter(x, y, c="red")
plt.scatter(x1, y1, c="green")
plt.scatter(x2, y2, c="black")
#plt.show()


pokemon= [[float(element1) for element1 in i] for i in pokemon] 


def ecd(x, y):
    distance = math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
    return distance

dist = [(ecd((a, b),(x,y)),c) for a,b in test for x, y, c in pokemon]
print(dist)

def pokemon_type():
    pass


# Rälna ut kortaste distansen med range mellan 1-150
# dinsten mellan range 151-300 m.m

# Skriv ut villken typ det är från test koordinaten x4.

