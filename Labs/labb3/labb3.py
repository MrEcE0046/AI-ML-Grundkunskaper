import numpy as np, matplotlib.pyplot as plt, csv

data = []
with open("unlabelled_data.csv") as f:
    rows = f.readlines()
    for row in rows:
        data.append([float(i) for i in row.split(",")])


x = 1
k = -1.2
m = 0
y = k*x+m

k = -1.2
m = 0
x = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
y = list()
for xval in x:
  y.append(k*xval + m)

def categories(y, data):
    data_label = []
    for yval in y:
        for i in data:
            if i[1] < yval:
                data_label.append((i[0], i[1], 0))
            else:
                data_label.append((i[0], i[1], 1))
    return data_label
         
       
label_data = categories(y, data)


zeros = [i for i in label_data if i[2] ==  0]
ones = [i for i in label_data if i[2] ==  1]



with open("labelled_data.csv", "w", newline="") as ld:
    writer = csv.writer(ld)
    writer.writerows(label_data)

plt.plot(x,y,"r")
#plt.scatter(*zip(*data))
plt.scatter(zeros[0], zeros[1], c= "blue")
plt.scatter(ones[0], ones[1], c="green")
plt.legend(("y=kx+m", "Label 0", "Label 1"))
plt.show()