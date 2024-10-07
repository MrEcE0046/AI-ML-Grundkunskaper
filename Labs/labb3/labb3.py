import numpy as np, matplotlib.pyplot as plt, csv

data = []
with open("unlabelled_data.csv") as f:
    rows = f.readlines()
    for row in rows:
        data.append([float(i) for i in row.split(",")])


# x = 5
# k = -1.2
# m = 0
# y = k*x+m # -6
# print(y) 

k = -1.2
m = 0
x = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
y = list()
for xval in x:
  y.append(k*xval + m)

def categories(y, data):
    k = -1.2
    m = 0
    
    data_label = []
    for x, y in data:
        val = k*x+m
        if y < val:
            data_label.append((x, y, 0))
        elif y > val:
            data_label.append((x, y, 1))
    return data_label

       
label_data = categories(y, data)
print(label_data)

zeroes = [i for i in label_data if i[2] ==  0] # Separerar 1/0 från stora listan, bara för att plotta
ones = [i for i in label_data if i[2] ==  1]

x_values = [item[0] for item in zeroes] # Separerar x och y för att slippa 0/1
y_values = [item[1] for item in zeroes]

x_value = [item[0] for item in ones] # Separerar x och y för att slippa 0/1
y_value = [item[1] for item in ones]

with open("labelled_data.csv", "w", newline="") as ld:
    writer = csv.writer(ld)
    writer.writerows(label_data)


#print(zeros)
#print(ones)
#print(label_data)
#print(data)
# print(len(label_data))
# print(len(zeroes))
# print(len(ones))

# plt.plot((-5, 6),(5, -6),"r")
plt.plot(x,y,"r")
plt.scatter(*zip(*data))
plt.scatter(x_value, y_value, c="blue")
plt.scatter(x_values, y_values, c= "green")
plt.legend(("y=kx+m", "Label 1", "Label 0"))
plt.show()