import numpy as np, matplotlib.pyplot as plt, math


pokemon = []
with open("datapoints.txt") as file:
    first_line = file.readline()
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
x3, y3 = zip(*pichu) 
x1, y1 = zip(*pikachu)

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

def ecd(x, y): # 
    distance = math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
    return distance


dist = [(ecd((a, b),(x,y)),c) for a,b in test for x,y, c in pokemon] 


def pokemon_type(dist): # Plockar in 4x150 distanser och tar den minsta för varje testpunkt. 
    distances = [(0, 150), (151, 300), (301, 450), (451, 600)]
    dist1= []
    for start, end in distances:
        dist1.append(min(dist[start:end + 1]))
    return dist1
    

label = pokemon_type(dist)

for i, y in zip(range(len(label)), test):
    if label[i][1] == 1:
        print(f"Sample with (width, height): {y} classified as Pikachu")
    else:
        print(f"Sample with (width, height): {y} classified as Pichu")

      
def user_input(pokemon): # Användaren lägger in en punkt och får reda på vilken typ
    pass
    while True:
        try:
            x = float(input("Skriv en koordinat på X-axeln: "))
            if 2 <= len(str(int(x))) <= 3:
                y = float(input("Skriv en koordinat på Y-axeln: "))
                if 2 <= len(str(int(y))) <= 3:
                    user_coordinate = [x, y]

                    distances = []
                    for i in pokemon:
                        distance = math.sqrt((i[0] - user_coordinate[0])**2 + (i[1] - user_coordinate[1])**2)
                        distances.append((distance, i[2]))
                    
                    distances.sort()
                    the_one_dist = distances[0]
                   
                    if the_one_dist[1] == 1:
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

#user_coordinate = user_input(pokemon) # Behövs denna funktionen?

def user_input_10near(pokemon): # Användaren lägger in en punkt och de tio närmsta avgör vilken typ det är
    while True:
        try:
            x = float(input("Skriv en koordinat på X-axeln: "))
            if 2 <= len(str(int(x))) <= 3:
                y = float(input("Skriv en koordinat på Y-axeln: "))
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

        
user_coordinate_10near = user_input_10near(pokemon)

plt.scatter(x3, y3, c="red")
plt.scatter(x1, y1, c="orange") # 
#plt.scatter(x2, y2, c="black") # Fyra test punkter
plt.scatter(user_coordinate_10near[0], user_coordinate_10near[1], c="black", marker="<")
plt.legend(("Pichu", "Pikachu", "test points", "user input"))
plt.show()

# Snygga till try, else except
# Lägg till gränser på punkt input
