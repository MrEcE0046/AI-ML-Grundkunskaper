import numpy as np, matplotlib.pyplot as plt, math

path = "datapoints.txt"
def datapoints(file):
    pokemon = []
    with open(file) as file:
        next(file)
        for line in file:
            x = line.strip().split(",")
            pokemon.append(x)

    pichu = [i for i in pokemon if i[2] == " 0"] # Sammlar alla pichu i en egen lista (alla som slutar på 0)
    pichu = [i[:-1] for i in pichu] # Tar bort sista elementet i den inre listan (tar bort alla nollor)
    pikachu = [i for i in pokemon if i[2] == " 1"]
    pikachu = [i[:-1] for i in pikachu]

    pokemon= [[float(element1) for element1 in i] for i in pokemon] #https://stackoverflow.com/questions/18072759/how-can-i-use-list-comprehensions-to-process-a-nested-list
    pichu = [[float(element) for element in i] for i in pichu] 
    pikachu = [[float(element) for element in i] for i in pikachu] 
    return pokemon, pichu, pikachu

test_points = "testpoints.txt"
def testpoints(test_points):
    test = []
    with open(test_points) as test_points: # Läser av testdata, rensar och placerar i lista
        next(test_points)
        # next(test_points) hoppar över första raden i filen?
        for line in test_points:
            t = line.split()
            test.append(t)

    test = [i[1:] for i in test] # Tar bort index i början för alla inre listor
    test = [[element.strip(",()") for element in i] for i in test] # Tar bort ', ' i dem inre listorna
    test= [[float(element1) for element1 in i] for i in test]
    return test


def pokemon_type(pokemon, test): # Plockar in 4x150 distanser och tar den minsta för varje testpunkt. 
    dist = []
    for p1, p2 in test:
        for q1, q2, label in pokemon:
            distance = math.sqrt((p1 - q1)**2 + (p2 - q2)**2)
            dist.append((distance, label))      

    distances = [(0, 150), (151, 300), (301, 450), (451, 600)]# banta ned till distance=range(0,600, 150)?
    dist1= []
    for start, end in distances:
        dist1.append(min(dist[start:end + 1]))
    
    for i, y in zip(range(len(dist1)), test):
        if dist1[i][1] == 1:
            print(f"Sample with (width, height): {y} classified as Pikachu")
        else:
            print(f"Sample with (width, height): {y} classified as Pichu")


def user_input(pokemon): # Användaren lägger in en punkt och får reda på vilken typ
    pass
    while True:
        try:
            x = float(input("Type the width between 15 - 30 of your pokemon: "))
            if 2 <= len(str(int(x))) <= 3:
                y = float(input("Type the height between 25 - 45 of your pokemon: "))
                if 2 <= len(str(int(y))) <= 3:
                    user_coordinate = [x, y]

                    distances = []
                    for i in pokemon:
                        distance = math.sqrt((i[0] - user_coordinate[0])**2 + (i[1] - user_coordinate[1])**2)
                        distances.append((distance, i[2]))
                    
                    distances.sort()
                    shortest_dist = distances[0]
                   
                    if shortest_dist[1] == 1:
                        print(f"Sample with (width, height): {x, y} classified as Pikachu")
                    else:
                        print(f"Sample with (width, height): {x, y} classified as Pichu")
                    
                    break
                else:
                    raise ValueError("Y-koordinaten måste vara 2-3 siffror lång.")
            else:
               raise ValueError("X-koordinaten måste vara 2-3 siffror lång.")
            
        except Exception as e:
            print("Ett fel inträffade:", e)


def user_input_10near(pokemon): # Användaren lägger in en punkt och de tio närmsta avgör vilken typ det är
    while True:
        try:
            x = float(input("Type the width between 15 - 30 of your pokemon: "))
            if 2 <= len(str(int(x))) <= 3:
                y = float(input("Type the height between 25 - 45 of your pokemon: "))
                if 2 <= len(str(int(y))) <= 3:
                    user_coordinate = [x, y]

                    distances = []
                    for i in pokemon:
                        distance = math.sqrt((i[0] - user_coordinate[0])**2 + (i[1] - user_coordinate[1])**2)
                        distances.append((distance, i[2]))
                    
                    distances.sort()
                    pikachu = 0
                   
                    for i in distances[:10]: 
                        if i[1] == 1:
                            pikachu += 1

                    if pikachu >= 5:
                        print(f"Sample with (width, height): {x, y} classified as Pikachu - 10 -")
                    else:
                        print(f"Sample with (width, height): {x, y} classified as Pichu - 10 -")
                    return user_coordinate
                   
                else:
                    raise ValueError("Y-koordinaten måste vara 2-3 siffror lång.")
            else:
               raise ValueError("X-koordinaten måste vara 2-3 siffror lång.")  
        except Exception as e:
            print("Ett fel inträffade:", e)


pokemon, pichu, pikachu = datapoints(path)
test = testpoints(test_points)
pokemon_type(pokemon, test)
input = user_input(pokemon)
#user_coordinate_10near = user_input_10near(pokemon)
print(pichu)
plt.scatter(*zip(*pichu), c="red")
plt.scatter(*zip(*pikachu), c="orange") # 
plt.scatter(*zip(*test), c="green") # Fyra test punkter
#plt.scatter(user_coordinate_10near[0], user_coordinate_10near[1], c="black", marker="<")
plt.legend(("Pichu", "Pikachu", "test points", "user input"))
plt.show()