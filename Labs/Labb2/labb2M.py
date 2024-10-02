import numpy as np, matplotlib.pyplot as plt, math, random as rnd

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
    while True:
        try:
            x = float(input("Type the width between 15 - 30 of your pokemon: "))
            if 15 <= x <= 30:
                y = float(input("Type the height between 25 - 45 of your pokemon: "))
                if 25 <= y <= 45:
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
                    return user_coordinate
                   
                else:
                    raise ValueError("The height must be between 25 - 45.")
            else:
                raise ValueError("The width must be between 15 - 30.")  
        except Exception as e:
            print("An error occurred:", e)
        


def user_input_10near(pokemon): # Användaren lägger in en punkt och de tio närmsta avgör vilken typ det är
    while True:
        try:
            x = float(input("Type the width between 15 - 30 of your pokemon: "))
            if 15 <= x <= 30:
                y = float(input("Type the height between 25 - 45 of your pokemon: "))
                if 25 <= y <= 45:
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
                    raise ValueError("The height must be between 25 - 45.")
            else:
                raise ValueError("The width must be between 15 - 30.")  
        except Exception as e:
            print("An error occurred:", e)

def random_data(pokemon):
    pichu_test = [i for i in pokemon if i[2] ==  0.0]
    pikachu_test = [i for i in pokemon if i[2] == 1.0]
    pichu_data_label = []
    pikachu_data_label = []
    rnd.shuffle(pichu_test)
    rnd.shuffle(pikachu_test)
    
    for i in range(50):
        pichu_data_label.append(pichu_test.pop(0)) # https://stackoverflow.com/questions/9406439/can-i-use-pop-and-append-on-the-same-item-at-the-same-time-in-python
        pikachu_data_label.append(pikachu_test.pop(0)) # Kopierar ett element ur pikachu_test och appendar i pikachu_data samtidigt som den tar bort elementet ur pikachu_test.
    
    pichu_test = [i[:-1] for i in pichu_test] # Ren testdata utan label
    pikachu_test = [i[:-1] for i in pikachu_test]
    pichu_data = [i[:-1] for i in pichu_data_label]
    pikachu_data = [i[:-1] for i in pikachu_data_label]
    print(pichu_data)

    plt.scatter(*zip(*pichu_data), c="red")   
    plt.scatter(*zip(*pikachu_data), c="orange") 
    plt.legend(("Pichu", "Pikachu", "test points", "user input"))
    plt.show()
    

def scatter_plot(input, pichu, pikachu, test,):
    plt.scatter(*zip(*pichu), c="red")   
    plt.scatter(*zip(*pikachu), c="orange") #   
    plt.scatter(*zip(*test), c="green") # Fyra test punkter 
    plt.scatter(input[0], input[1], c="black", marker="<") 
    #plt.scatter(user_coordinate_10near[0], user_coordinate_10near[1], c="black", marker="<") 
    plt.legend(("Pichu", "Pikachu", "test points", "user input"))
    plt.show()
    

pokemon, pichu, pikachu = datapoints(path)
test = testpoints(test_points)
pokemon_type(pokemon, test)

while True:
    try:
        menu = int(input("\n1. Clasify a Pokemon by the nearest nabor.\n2. Classify the pokemon by the ten nearest nabor.\n3. Get the accuracy of the data.\n4. Quit\n:"))
        if menu == 1:
            input2 = user_input(pokemon)
            plot = scatter_plot(input2, pichu, pikachu, test)
        if menu == 2:
            user_coordinate_10near = user_input_10near(pokemon)
            plot1 = scatter_plot(user_coordinate_10near, pichu, pikachu, test)
        elif menu == 3:
            random = random_data(pokemon)
        elif menu == 4:
            print("Quiting")
            break
        else:
            print("Not a valid key")
    except (ValueError, TypeError):
        pass