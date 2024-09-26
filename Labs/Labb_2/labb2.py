import matplotlib.pyplot as plt

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

x, y = zip(*pichu) # https://stackoverflow.com/questions/21519203/plotting-a-list-of-x-y-coordinates#:~:text=I%20have%20a%20list%20of%20pairs%20(a,%20b)%20that%20I
x1, y1 = zip(*picatchu)
plt.scatter(x, y, c="red")
plt.scatter(x1, y1, c="blue")
#plt.show()

test = []
with open("testpoints.txt") as test_points:
    first_line = test_points.readline()
    for line in test_points:
        x = line.split()
        test.append(x)

test = [i[1:] for i in test]
test = [[element.strip(', ') for element in i] for i in test]
x2, y2 = zip(*test)


print(y2)










#dist = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
   