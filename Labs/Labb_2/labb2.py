#scatterplot
import os
os.getcwd()

dice_value = {"width", "height", "label"}

with open("datapoints.txt") as file:
    for line in file:
        parts = line.split()

        width = int(parts[0])
        height = int(parts[1])
        label = int(parts[2])


with open("datapoints.txt") as file:
    print(file.read()) # read whole file
